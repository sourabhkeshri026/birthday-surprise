import streamlit as st
import base64
from pathlib import Path

st.set_page_config(
    page_title="Happy Birthday Tanya ❤️",
    page_icon="🎂",
    layout="wide"
)

if "opened" not in st.session_state:
    st.session_state.opened = False


st.markdown("""
<style>

#MainMenu{visibility:hidden;}
header{visibility:hidden;}
footer{visibility:hidden;}

.stApp{
background:linear-gradient(135deg,#fff0f5,#ffe4ec,#fff8f9);
}

.main{
text-align:center;
}

.title{
margin-top:140px;
font-size:70px;
font-weight:bold;
color:#ff2d55;
text-align:center;
}

.subtitle{
font-size:28px;
text-align:center;
color:#666;
margin-bottom:60px;
}

.stButton>button{
display:block;
margin:auto;
background:#ff2d55;
color:white;
font-size:26px;
padding:15px 45px;
border-radius:15px;
border:none;
}

.stButton>button:hover{
background:#ff4f6d;
}
.rose{
position:fixed;
top:-10%;
font-size:32px;
animation:fall linear infinite;
z-index:999;
pointer-events:none;
}

@keyframes fall{

0%{
transform:translateY(-100px) rotate(0deg);
opacity:1;
}

100%{
transform:translateY(110vh) rotate(360deg);
opacity:0.8;
}

}
</style>
""",unsafe_allow_html=True)

if not st.session_state.opened:

    st.markdown(
        "<div class='title'>🎂 Happy Birthday Tanya ❤️</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='subtitle'>A little surprise is waiting for you...</div>",
        unsafe_allow_html=True
    )

    if st.button("🎁 Open My Surprise"):
        st.session_state.opened=True
        st.rerun()

else:

    # 🌹 Falling Roses
    rose_html = ""

    positions = [5,15,25,35,45,55,65,75,85,95]
    durations = [8,9,10,11,7,12,8,10,9,11]

    for left, duration in zip(positions, durations):

        rose_html += f"""
        <div class='rose'
        style='left:{left}%;
        animation-duration:{duration}s;
        animation-delay:-{duration/2}s'>
        🌹
        </div>
        """

    st.markdown(rose_html, unsafe_allow_html=True)

    # 🎈 Balloons
    st.balloons()

    # 🎂 Title
    st.markdown("""
    <h1 style='text-align:center;
    color:#ff2d55;
    font-size:60px;'>
    Happy Birthday Tanya ❤️
    </h1>
    """, unsafe_allow_html=True)

    # 📷 Center Image
    col1, col2, col3 = st.columns([1,2,1])

    with col2:

        with open("assets/tanya.jpeg", "rb") as img:
            img_base64 = base64.b64encode(img.read()).decode()

        st.markdown(f"""
        <div style="text-align:center;">
        <img src="data:image/jpeg;base64,{img_base64}"
        style="
        width:350px;
        border-radius:25px;
        border:6px solid white;
        box-shadow:0px 0px 35px rgba(255,105,180,0.6);
        ">
        </div>
        """, unsafe_allow_html=True)

    # 💌 Birthday Message
    st.markdown("""
    <div style="
    text-align:center;
    font-size:28px;
    padding:25px;
    line-height:1.8;
    color:#444;
    max-width:900px;
    margin:auto;
    ">

    💖

    May your smile always stay this beautiful.

    May every dream you have come true.

    May happiness always find its way to you.

    Thank you for being such a wonderful person.

    I hope today brings you endless joy,
    countless beautiful memories,
    and everything your heart wishes for.

    🌹 Happy Birthday Tanya 🌹

    Stay blessed.
    Keep smiling.
    Enjoy your special day! ❤️

    </div>
    """, unsafe_allow_html=True)

    # 🎵 Music Player
    st.markdown("### 🎵 Birthday Song")

    audio_file = open("assets/birthday.mp3", "rb")
    audio_bytes = audio_file.read()

    st.audio(audio_bytes, format="audio/mp3")