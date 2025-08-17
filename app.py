import streamlit as st
from summarize import summarize_text
import time
import random
from gtts import gTTS
import io

st.set_page_config(page_title="Student Text Summarizer", page_icon="📘", layout="centered")

st.markdown("""
    <style>
        .title-text {
            font-size: 2.3em;
            font-weight: 600;
            color: #66b3ff;
        }
        .footer {
            text-align: center;
            font-size: 1.5em;
            color: gray;
            margin-top: 50px;
        }
        .summary-box {
            background-color: #1e1e1e;
            color: #f0f0f0;
            padding: 15px;
            border-radius: 10px;
        }
        .tips-box {
            background-color: #2a2a2a;
            color: #dddddd;
            padding: 10px;
            border-left: 5px solid #66b3ff;
            border-radius: 5px;
        }
    </style>
""", unsafe_allow_html=True)


st.markdown("<div class='title-text'>📘 AI-Powered Student Text Summarizer</div>", unsafe_allow_html=True)
st.caption("Choose between LSA, LexRank, or Luhn to summarize your academic content in seconds.")

st.divider()

tips = [
    "Use it for summarizing lecture notes or PDFs.",
    "Try summarizing articles in different styles to compare results.",
    "Combine summaries from multiple methods for better understanding.",
    "Shorter summaries are great for revision notes!"
]
st.markdown(f"<div class='tips-box'>💡 Tip: {random.choice(tips)}</div>", unsafe_allow_html=True)
st.write("")

col1, col2 = st.columns([3, 1])
with col1:
    input_text = st.text_area("✍️ Enter your content:", height=250)
with col2:
    method = st.selectbox("🧠 Method", ["LSA", "LexRank", "Luhn"])
    num_sentences = st.slider("🔢 Summary Sentences", 1, 10, 3)

if st.button("🚀 Generate Summary"):
    if input_text.strip():
        with st.spinner(f"Generating summary using **{method}**..."):
            time.sleep(0.5)
            summary = summarize_text(input_text, method=method, num_sentences=num_sentences)

            words = len(summary.split())
            read_time = round(words / 200, 2)

            st.markdown("### 📌 Summary:")
            st.markdown(f"<div class='summary-box'>{summary}</div>", unsafe_allow_html=True)

            st.markdown(f"🕒 Estimated reading time: **{read_time} minute(s)**")
            st.download_button("⬇️ Download Summary", summary, file_name="summary.txt")
            tts = gTTS(summary)
            mp3_fp = io.BytesIO()
            tts.write_to_fp(mp3_fp)
            mp3_fp.seek(0)

            st.audio(mp3_fp, format="audio/mp3", start_time=0)
            st.download_button("🔊 Download Audio", mp3_fp, file_name="summary.mp3", mime="audio/mpeg")
    else:
        st.warning("⚠️ Please enter some text to summarize.")

st.markdown("<div class='footer'>Made By Tanish Maheshwari 22BIT0013</div>", unsafe_allow_html=True)
