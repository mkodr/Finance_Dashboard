import streamlit as st
import streamlit.components.v1 as components
import json
import os
import random


# =====================================================
# PAGE SETTINGS
# =====================================================

st.set_page_config(
    page_title="Classical Music Explorer",
    page_icon="🎼",
    layout="wide"
)



# =====================================================
# LOAD DATABASE
# =====================================================

@st.cache_data
def load_music():

    with open(
        "composers.json",
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)



music = load_music()



# =====================================================
# SESSION STATE
# =====================================================

if "favorites" not in st.session_state:

    st.session_state.favorites = []



# =====================================================
# CSS DESIGN
# =====================================================

st.markdown("""

<style>


.stApp {

background:
linear-gradient(
135deg,
#090d12,
#111827
);

}



h1 {

color:#f4d35e;

font-size:50px;

}



h2 {

color:#f4d35e;

}



.card {


background:

linear-gradient(
145deg,
#161b22,
#10151c
);


border-radius:20px;

padding:25px;

border:

1px solid #30363d;


margin-bottom:25px;


}



.composer-name {


font-size:32px;

font-weight:bold;

color:#f4d35e;


}



.tag {


background:#273142;

padding:6px 12px;

border-radius:20px;

font-size:13px;

}



.info {


color:#bbbbbb;

font-size:15px;

}



button {


border-radius:20px!important;


}



</style>

""",
unsafe_allow_html=True)




# =====================================================
# SIDEBAR
# =====================================================


st.sidebar.title("🎼 Music Explorer")


era = st.sidebar.selectbox(

    "Choose Musical Period",

    list(music.keys())

)



st.sidebar.markdown("---")



search = st.sidebar.text_input(

    "🔎 Search composer"

)



st.sidebar.markdown("---")



if st.sidebar.button("🎲 Random Composer"):


    all_composers=[]


    for period in music.values():

        all_composers.extend(
            period["composers"]
        )


    choice=random.choice(all_composers)


    st.session_state.random = choice["name"]




# =====================================================
# HEADER
# =====================================================


period = music[era]


st.title(
    "🎼 Classical Music Explorer"
)



st.markdown(

f"""

<div class="card">


<h2>{era}</h2>


<p class="info">

{period['years']}

</p>


<p>

{period['description']}

</p>


</div>


""",

unsafe_allow_html=True

)




# =====================================================
# COMPOSER DISPLAY
# =====================================================


for composer in period["composers"]:



    name = composer["name"]



    # Search filtering

    if search:

        if search.lower() not in name.lower():

            continue



    # -------------------------------------------------

    st.markdown(

    f"""

    <div class="card">


    <div class="composer-name">

    {name}

    </div>


    <br>


    <span class="tag">

    {composer['style']}

    </span>


    <br><br>


    <p class="info">

    Born: {composer['birth']}

    </p>


    <p>

    {composer['about']}

    </p>


    </div>

    """,

    unsafe_allow_html=True

    )



    # -------------------------------------------------
    # IMAGE SUPPORT
    # -------------------------------------------------


    image_path = (

        "images/" +

        composer["image"]

    )



    if os.path.exists(image_path):

        st.image(

            image_path,

            width=250

        )



    else:

        st.info(
            "Add image: " + image_path
        )




    # -------------------------------------------------
    # FAVORITES
    # -------------------------------------------------


    if st.button(

        "⭐ Favorite " + name,

        key="fav_"+name

    ):


        if name not in st.session_state.favorites:

            st.session_state.favorites.append(name)



    # -------------------------------------------------
    # MUSIC PLAYER
    # -------------------------------------------------


    st.subheader(
        "🎧 Listen"
    )



    songs = {}


    for song in composer["songs"]:

        songs[
            song["title"]
        ] = song["youtube"]




    selected_song = st.selectbox(

        "Choose a piece",

        list(songs.keys()),

        key=name

    )



    youtube_url = songs[selected_song]



    # Extract search URL into embed style

    video_search = (

        youtube_url

        .replace(
            "https://www.youtube.com/results?search_query=",
            ""
        )

    )


    st.markdown(

    f"""

    <a href="{youtube_url}" target="_blank">

    ▶ Open YouTube Search:
    {selected_song}

    </a>

    """,

    unsafe_allow_html=True

    )



    components.html(

    f"""

    <iframe

    width="100%"

    height="400"

    src="https://www.youtube.com/embed?listType=search&list={video_search}"

    frameborder="0"

    allowfullscreen>

    </iframe>

    """,

    height=420

    )



    st.divider()




# =====================================================
# FAVORITES PANEL
# =====================================================


st.sidebar.markdown("---")

st.sidebar.subheader(
    "⭐ Favorites"
)


if st.session_state.favorites:


    for fav in st.session_state.favorites:

        st.sidebar.write(
            "🎵 " + fav
        )

else:

    st.sidebar.write(
        "No favorites yet"
    )
