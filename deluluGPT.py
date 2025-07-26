import streamlit as st
import openai
import os
from dotenv import load_dotenv
load_dotenv()  # Load from .env into environment

# Safely get your API key
API_KEY = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=API_KEY)


st.set_page_config(page_title="Delulu GPT", page_icon="🌈", layout="centered")


st.markdown("""
    <style>
    .title-text {
        font-size: 2.5em;
        text-align: center;
        font-family: 'Comic Sans MS', cursive;
        color: #ff69b4;
        text-shadow: 2px 2px #000;
    }
    .mode-button {
        border-radius: 50px;
        border: none;
        padding: 1em 2em;
        margin: 1em;
        font-size: 1.2em;
        background-color: #ff00ff55;
        cursor: pointer;
        box-shadow: 0 0 10px #fff;
    }
    .parchment-prophecy {
        font-size: 1.4em;
        font-style: italic;
        color: #4b3f2f;
        background: url('https://www.transparenttextures.com/patterns/paper-fibers.png');
        background-color: #fef8e3;
        padding: 30px;
        border-radius: 12px;
        border: 2px solid #d8caa0;
        box-shadow: 0 0 30px rgba(0,0,0,0.1);
        text-align: center;
        opacity: 0;
        animation: fadeInScroll 2s ease-in-out forwards;
    }


    @keyframes fadeInScroll {
        0%   { opacity: 0; transform: translateY(20px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    </style>
""", unsafe_allow_html=True)


st.markdown("<div class='title-text'>Welcome to Delulu GPT 🚀</div>", unsafe_allow_html=True)


st.markdown("**Where reality is a suggestion.**")


user_input = st.text_area("What's your intrusive thought, fear, or dream?", placeholder="e.g., I'm not smart enough for tech")


col1, col2 = st.columns([1, 1])
with col1:
    reality = st.button("🧠 Reality Mode")
with col2:
    delulu = st.button("🌟 Delulu Mode")


# Function to query GPT with different prompts
def get_gpt_response(mode, user_input):
    if mode == "reality":
        prompt = f"You are a wise, emotionally intelligent tech mentor. Respond to this with warmth and practical advice: '{user_input}'"
    else:
        prompt = f"You are a delusionally confident, over-the-top hype queen AI. Respond to this with absolute chaos and maximum confidence: '{user_input}'"


    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are an emotionally resonant, creative chatbot."},
            {"role": "user", "content": prompt}
        ],
        temperature=1.1,
        max_tokens=150
    )
    return response.choices[0].message.content


if user_input:
    if reality:
        st.markdown("### 🧠 Reality Mode Says:")
        with st.spinner("Connecting to reality..."):
            response = get_gpt_response("reality", user_input)
            st.markdown(f"<div class='parchment-prophecy'>{response}</div>", unsafe_allow_html=True)


    if delulu:
        st.markdown("### 🌟 Delulu Mode Screams:")
        with st.spinner("Summoning delusion..."):
            response = get_gpt_response("delulu", user_input)
            st.balloons()
            st.markdown(f"<div style='font-size:1.5em; color:#ff1493; font-style:italic'>{response}</div>", unsafe_allow_html=True)


st.markdown("---")
st.markdown("<center><small>Made with delusion, dreams, and Python 🦋</small></center>", unsafe_allow_html=True)



