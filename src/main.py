import streamlit as st
from translator_utils import translate

st.set_page_config(
    page_title="Translator-AI",
    page_icon="📝",
    layout="centered"
)

st.title("🗺️ Siddha Translator App 🗺️")

col1, col2 = st.columns(2)

with col1:
    input_lang = st.selectbox(
        "Input Language",
        ['English', 'French', 'Spanish', 'German', 'Latin', 'Hindi', 'Bengali', 'Tamil', 'Telugu']
    )

with col2:
    output_lang_list = [lang for lang in
        ['English', 'French', 'Spanish', 'German', 'Latin', 'Hindi', 'Bengali', 'Tamil', 'Telugu']
        if lang != input_lang]
    output_lang = st.selectbox("Output Language", output_lang_list)

input_text = st.text_area("Type the text to be translated")

if st.button("Translate"):
    translated_text = translate(input_lang, output_lang, input_text)
    st.success(translated_text)