import streamlit as st
import urllib.parse
import streamlit.components.v1 as components


# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Classical Music Explorer",
    page_icon="🎼",
    layout="wide"
)


# =====================================================
# CUSTOM CSS
# =====================================================

st.markdown("""
<style>

html, body, [class*="css"] {
    font-family: 'Segoe UI', sans-serif;
}


.stApp {
    background:#0b0f14;
    color:white;
}


h1 {
    color:#f4d35e;
    font-size:48px;
}


h2 {
    color:#f4d35e;
}


.card {

background:
linear-gradient(
135deg,
#151b25,
#10151d
);

padding:25px;

border-radius:20px;

border:
1px solid #273142;

margin-bottom:20px;

}


.title {

font-size:30px;

font-weight:bold;

color:#f4d35e;

}


.subtitle {

color:#aaaaaa;

font-size:15px;

}


.song {

background:#1c2533;

padding:12px;

border-radius:12px;

margin-top:10px;

}


a {

color:#f4d35e;

text-decoration:none;

font-weight:bold;

}


</style>
""",
unsafe_allow_html=True)



# =====================================================
# MUSIC DATABASE
# =====================================================


music = {


"Baroque": [

{
"name":"Johann Sebastian Bach",

"style":"Counterpoint / Organ / Orchestra",

"about":
"German master of harmony and counterpoint. His works represent the peak of Baroque musical architecture.",

"songs":[

("Brandenburg Concerto No. 3",
"https://www.youtube.com/watch?v=hZ9qWpa2rIg"),

("Cello Suite No.1",
"https://www.youtube.com/watch?v=1prweT95Mo0"),

("Toccata and Fugue",
"https://www.youtube.com/watch?v=ho9rZjlsyYY")

]

},


{
"name":"Antonio Vivaldi",

"style":"Violin Concerto",

"about":
"Venetian composer famous for energetic concertos and especially The Four Seasons.",

"songs":[

("Spring - Four Seasons",
"https://www.youtube.com/watch?v=mFWQgxXM_b8"),

("Summer - Four Seasons",
"https://www.youtube.com/watch?v=Z21_VpN8v2I")

]

}


],



"Classical":[


{
"name":"Wolfgang Amadeus Mozart",

"style":"Symphony / Opera / Chamber",

"about":
"A child prodigy who created some of the most recognizable melodies in history.",

"songs":[

("Eine kleine Nachtmusik",
"https://www.youtube.com/watch?v=oy2zDJPIgwc"),

("Symphony No.40",
"https://www.youtube.com/watch?v=JTc1mDieQI8"),

("The Magic Flute",
"https://www.youtube.com/watch?v=YuBeBjqKSGQ")

]

},


{
"name":"Joseph Haydn",

"style":"Symphony / String Quartet",

"about":
"Known as the father of the symphony and string quartet.",

"songs":[

("Surprise Symphony",
"https://www.youtube.com/watch?v=tF5kr251BRs")

]

}


],



"Romantic":[


{
"name":"Ludwig van Beethoven",

"style":"Symphony / Piano",

"about":
"The revolutionary composer who transformed Classical music into Romantic expression.",

"songs":[

("Symphony No.5",
"https://www.youtube.com/watch?v=fOk8Tm815lE"),

("Moonlight Sonata",
"https://www.youtube.com/watch?v=4Tr0otuiQuU"),

("Symphony No.9",
"https://www.youtube.com/watch?v=t3217H8JppI")

]

},



{
"name":"Pyotr Tchaikovsky",

"style":"Orchestra / Ballet",

"about":
"Russian Romantic composer famous for dramatic melodies and ballet masterpieces.",

"songs":[

("Swan Lake",
"https://www.youtube.com/watch?v=9cNQFB0TDfY"),

("1812 Overture",
"https://www.youtube.com/watch?v=VbxgYlcNxE8")

]

}

],



"Impressionist / Modern":[


{
"name":"Claude Debussy",

"style":"Impressionism",

"about":
"Created atmospheric music using new harmonies and unusual tonal colors.",

"songs":[

("Clair de Lune",
"https://www.youtube.com/watch?v=CvFH_6DNRCY")

]

},



{
"name":"Igor Stravinsky",

"style":"Modernism",

"about":
"Changed 20th century music with revolutionary rhythm and orchestration.",

"songs":[

("The Rite of Spring",
"https://www.youtube.com/watch?v=EkwqPJZe8ms")

]

}

]


}



# =====================================================
# SIDEBAR
# =====================================================


st.sidebar.title("🎼 Music Library")

era = st.sidebar.radio(
    "Choose an Era",
    list(music.keys())
)


st.sidebar.markdown("---")

st.sidebar.write(
"""
Explore famous composers,
listen to masterpieces,
and discover musical history.
"""
)



# =====================================================
# HEADER
# =====================================================


st.title("🎼 Classical Music Explorer")

st.markdown(
f"""
<div class="card">

<div class="title">
{era} Era
</div>

<div class="subtitle">
Explore composers and listen to their greatest works.
</div>

</div>
""",
unsafe_allow_html=True
)



# =====================================================
# COMPOSER DISPLAY
# =====================================================


for composer in music[era]:


    st.markdown(
    f"""
    <div class="card">

    <div class="title">
    {composer['name']}
    </div>

    <p>
    <b>Style:</b>
    {composer['style']}
    </p>

    <p>
    {composer['about']}
    </p>

    </div>

    """,
    unsafe_allow_html=True
    )


    # SONG SELECTOR

    songs = {}

    for title,url in composer["songs"]:
        songs[title]=url



    selected = st.selectbox(
        f"🎧 Choose a {composer['name']} piece",
        list(songs.keys())
    )


    video_url = songs[selected]



    # Extract YouTube ID

    video_id = video_url.split("v=")[-1]



    # Custom YouTube Embed

    html = f"""

    <iframe

    width="100%"

    height="400"

    src="https://www.youtube.com/embed/{video_id}"

    frameborder="0"

    allow="autoplay; encrypted-media"

    allowfullscreen>

    </iframe>

    """



    components.html(
        html,
        height=420
    )


    st.markdown("---")



# =====================================================
# FOOTER
# =====================================================

st.markdown(
"""
<center>

🎻 Built with Python + Streamlit

</center>
""",
unsafe_allow_html=True
)
