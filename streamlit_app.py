import streamlit as st
import time
import random


# =====================================================
# CONFIGURATION
# =====================================================

WIDTH = 45
HEIGHT = 25

FRAME_TIME = 0.12


# =====================================================
# STREAMLIT CONFIG
# =====================================================

st.set_page_config(
    page_title="ASCII Space Invaders",
    layout="centered"
)


# =====================================================
# GAME OBJECTS
# =====================================================

class Player:

    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT - 2
        self.lives = 3
        self.symbol = "^"

    def move_left(self):
        self.x = max(1, self.x - 1)

    def move_right(self):
        self.x = min(WIDTH - 2, self.x + 1)


class StarField:

    def __init__(self):
        self.stars = []

        for i in range(40):
            self.stars.append(
                [
                    random.randint(1, WIDTH-2),
                    random.randint(1, HEIGHT-2)
                ]
            )

    def update(self):

        for star in self.stars:

            star[1] += 1

            if star[1] >= HEIGHT:
                star[0] = random.randint(1, WIDTH-2)
                star[1] = 1


# =====================================================
# GAME STATE
# =====================================================

class Game:

    def __init__(self):

        self.player = Player()

        self.stars = StarField()

        self.score = 0

        self.running = True


    def update(self):

        self.stars.update()


    def draw(self):

        screen = [
            [" " for x in range(WIDTH)]
            for y in range(HEIGHT)
        ]


        # stars

        for star in self.stars.stars:

            x,y = star

            if 0 <= x < WIDTH and 0 <= y < HEIGHT:
                screen[y][x] = "."


        # player

        screen[
            self.player.y
        ][
            self.player.x
        ] = self.player.symbol


        # convert to text

        output = ""

        output += "+" + "-"*WIDTH + "+\n"


        for row in screen:

            output += "|"

            output += "".join(row)

            output += "|\n"


        output += "+" + "-"*WIDTH + "+"

        return output



# =====================================================
# SESSION STATE
# =====================================================

if "game" not in st.session_state:

    st.session_state.game = Game()

    st.session_state.last_frame = time.time()



# =====================================================
# TITLE
# =====================================================

st.title("👾 ASCII SPACE INVADERS")

st.caption(
    "Part 1 - Engine Initialization"
)


game = st.session_state.game



# =====================================================
# CONTROLS
# =====================================================

left,right,restart = st.columns(3)


with left:

    if st.button("⬅ MOVE LEFT"):

        game.player.move_left()


with right:

    if st.button("MOVE RIGHT ➡"):

        game.player.move_right()


with restart:

    if st.button("🔄 Restart"):

        st.session_state.game = Game()

        st.rerun()



# =====================================================
# GAME DISPLAY
# =====================================================

game.update()


screen = game.draw()


st.code(screen)



# =====================================================
# STATUS
# =====================================================

st.write(
    f"""
    Score: {game.score}  
    Lives: {game.player.lives}
    """
)



# =====================================================
# AUTO REFRESH LOOP
# =====================================================

time.sleep(FRAME_TIME)

st.rerun()
