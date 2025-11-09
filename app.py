import streamlit as st
from deep_translator import GoogleTranslator
import pyperclip

# Page setup
st.set_page_config(page_title="AI Translator", page_icon="🌍", layout="centered")
st.title("🌍 AI Translator")
st.write("Translate text between multiple languages instantly.")

# Language mapping
languages = {
    'Auto': 'auto',
    'English': 'en',
    'Hindi': 'hi',
    'Tamil': 'ta',
    'French': 'fr',
    'Spanish': 'es',
    'German': 'de',
    'Japanese': 'ja',
    'Korean': 'ko',
    'Chinese': 'zh-CN'
}

# UI elements
col1, col2 = st.columns(2)
with col1:
    src_lang_name = st.selectbox("Source language:", list(languages.keys()), index=0)
with col2:
    tgt_lang_name = st.selectbox("Target language:", list(languages.keys()), index=1)

# Text input
text = st.text_area("Enter text to translate:", height=150)

# Translate button
if st.button("Translate 🔄"):
    if text.strip():
        try:
            translated = GoogleTranslator(
                source=languages[src_lang_name],
                target=languages[tgt_lang_name]
            ).translate(text)
            st.text_area("Translated text:", value=translated, height=150, key="output")
            st.session_state['translated_text'] = translated
        except Exception as e:
            st.error(f"Translation failed: {e}")
    else:
        st.warning("Please enter some text!")

# Buttons for extra actions
col3, col4 = st.columns(2)
with col3:
    if st.button("Clear"):
        st.session_state.clear()
        st.experimental_rerun()

with col4:
    if 'translated_text' in st.session_state:
        if st.button("Copy to Clipboard 📋"):
            pyperclip.copy(st.session_state['translated_text'])
            st.success("Copied translated text to clipboard!")

st.markdown("---")
st.caption("Made with ❤️ by Janadharshini")
