import streamlit as st
import base64
from pathlib import Path
import streamlit.components.v1 as components
import random 

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

.envelope-wrapper{
display:flex;
justify-content:center;
margin-top:40px;
margin-bottom:30px;
}

.envelope{

width:340px;
height:220px;
position:relative;
cursor:pointer;
transition:.4s;
}

.envelope:hover{

transform:scale(1.05);

}

.envelope-body{

position:absolute;

bottom:0;

width:340px;
height:170px;

background:#FFF8E7;

border-radius:0 0 18px 18px;

box-shadow:0 15px 35px rgba(0,0,0,.18);

}

.envelope-flap{

position:absolute;

top:0;

width:0;
height:0;

border-left:170px solid transparent;
border-right:170px solid transparent;
border-top:120px solid #FFD6A5;

transform-origin:top;

transition:1s;

z-index:10;

}

.envelope:hover .envelope-flap{

transform:rotateX(180deg);

}

.envelope-text{

position:absolute;

bottom:55px;

width:100%;

text-align:center;

font-size:28px;

font-weight:bold;

color:#d63384;

z-index:20;

}

.letter-card{

background:#FFF8E7;

padding:40px;

border-radius:25px;

box-shadow:0 15px 35px rgba(0,0,0,.15);

font-size:25px;

line-height:2;

color:#6D3FB7;

max-width:900px;

margin:auto;

animation:letterAppear 1.2s;

}

@keyframes letterAppear{

0%{

opacity:0;
transform:translateY(60px);

}

100%{

opacity:1;
transform:translateY(0);

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

    col1, col2, col3 = st.columns([2,3,2])

    with col2:
        if st.button("🎀 Unwrap Your Surprise", use_container_width=True):
            st.session_state.opened = True
            st.rerun()

else:

    # 🌹 Falling Roses
    rose_html = ""

    positions = list(range(2,100,4))
    durations = [random.randint(6,12) for _ in positions]
    items = ["🌹","🌻","🍫","🎈","💖","✨","🎁","🍰"]

    for left, duration in zip(positions, durations):

        rose_html += f"""
        <div class='rose'
        style='left:{left}%;
        animation-duration:{duration}s;
        animation-delay:-{duration/2}s'>
        {random.choice(items)}
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
    if "letter_opened" not in st.session_state:
        st.session_state.letter_opened = False

    st.markdown("""
    <h2 style="text-align:center;color:#ff2d55;">
    💌 A Letter Just For Tanya
    </h2>
    """, unsafe_allow_html=True)

    if not st.session_state.letter_opened:

        st.markdown("""

    <div class="envelope-wrapper">

    <div class="envelope">

    <div class="envelope-flap"></div>

    <div class="envelope-body"></div>

    <div class="envelope-text">

    💌

    <br>

    Tap the button below
    <br>
    to open your letter ❤️

    </div>

    </div>

    </div>

    """, unsafe_allow_html=True)

        col1,col2,col3=st.columns([2,2,2])

        with col2:

            if st.button("💌 Open My Letter",use_container_width=True):

                st.session_state.letter_opened=True

                st.rerun()

    else:

        st.markdown("""

    <div class="letter-card">

    <h2 style="text-align:center;color:#d63384;">
    🌸 Dear Tanya 🌸
    </h2>

    May your smile always stay this beautiful. ❤️

    <br><br>

    May every dream you have come true.

    <br><br>

    May happiness always find its way to you.

    <br><br>

    Thank you for being such a wonderful person.

    <br><br>

    I hope today brings you endless joy,
    countless beautiful memories,
    and everything your heart wishes for.

    <br><br>

    <div style="text-align:center;font-size:34px;">

    🌹 Happy Birthday Tanya 🌹

    </div>

    <br>

    Stay blessed.

    <br>

    Keep smiling.

    <br>

    Enjoy your special day! ❤️

    </div>

    """, unsafe_allow_html=True)

        # 🎵 Music Player
        st.markdown("### 🎵 Birthday Song")

        audio_file = open("assets/birthday.mp3", "rb")
        audio_bytes = audio_file.read()

        st.audio(audio_bytes, format="audio/mp3")

        components.html("""
        <style>

        body{
            background:transparent;
            font-family:Arial;
        }

        .lyrics{
            max-width:850px;
            margin:auto;
            margin-top:20px;
        }

        .verse{
            padding:18px;
            margin:18px 0;
            border-radius:18px;
            font-size:24px;
            color:#666;
            transition:all .8s ease;
        }

        .active{
            background:#ffe8ef;
            color:#ff2d55;
            font-weight:bold;
            transform:scale(1.02);
            box-shadow:0 0 25px rgba(255,105,180,.45);
        }

        </style>

        <h2 style="text-align:center;color:#ff2d55;">
        🎤 Lyrics
        </h2>

        <div class="lyrics">

        <div class="verse active">
        <b>Verse 1</b><br><br>

        Today the sun is shining bright,<br>
        Just to celebrate your light.<br>
        Every smile you share each day,<br>
        Makes the clouds all fade away.<br><br>

        You bring laughter everywhere,<br>
        With your kindness and your care.<br>
        May this birthday bring to you,<br>
        Every dream you've wished comes true.
        </div>

        <div class="verse">
        <b>Chorus</b><br><br>

        Happy Birthday, Tanya,<br>
        This day belongs to you.<br>
        May your heart be filled with joy,<br>
        And all your dreams come true.<br><br>

        Keep on smiling every day,<br>
        Just the way you always do.<br>
        The world is brighter, happier,<br>
        Simply because of you.
        </div>

        <div class="verse">
        <b>Verse 2</b><br><br>

        May your journey always lead<br>
        To every hope and every dream.<br>
        May every step you choose to take<br>
        Become a beautiful memory.<br><br>

        May your laughter never fade,<br>
        May your heart stay full of light.<br>
        May love and happiness surround<br>
        Your every day and every night.
        </div>

        <div class="verse">
        <b>Chorus</b><br><br>

        Happy Birthday, Tanya,<br>
        May your future shine so bright.<br>
        May every little wish you make<br>
        Fill your world with light.<br><br>

        Keep believing in yourself,<br>
        You're stronger than you know.<br>
        May every year that comes your way<br>
        Help your beautiful heart grow.
        </div>

        <div class="verse">
        <b>Bridge</b><br><br>

        When life becomes a little hard,<br>
        Remember how amazing you are.<br>
        Keep your faith, keep chasing dreams,<br>
        You'll always be a shining star.<br><br>

        Wherever life may take you next,<br>
        May happiness walk by your side.<br>
        And may today remind you<br>
        How loved you are inside.
        </div>

        <div class="verse">
        <b>Final Chorus</b><br><br>

        Happy Birthday, Tanya,<br>
        May your smile never fade.<br>
        May every dream you dream today<br>
        Become the life you've made.<br><br>

        Here's to laughter, love and hope,<br>
        And every joy that's still to come.<br>
        Happy Birthday, Tanya dear,<br>
        Your best days have just begun.<br><br>

        ❤️ Happy Birthday Tanya ❤️
        </div>

        </div>

        <script>

        const verses=document.querySelectorAll(".verse");

        let current=0;

        function glow(){

            verses.forEach(v=>v.classList.remove("active"));

            verses[current].classList.add("active");

            verses[current].scrollIntoView({

                behavior:"smooth",

                block:"center"

            });

            current++;

            if(current<verses.length){

                setTimeout(glow,25000);

            }

        }

        setTimeout(glow,25000);

        </script>

        """,height=900)
