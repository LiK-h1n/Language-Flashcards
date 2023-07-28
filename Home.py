import streamlit as st
from word import get_random_word
from translator import translate
from supported_languages import get_language_codes
from speech_service import get_speech


def show_word_or_translation(value, button_needed=False):
    st.markdown("-----")
    st.subheader(value)
    if button_needed:
        button = st.button("PRONOUNCE")
    st.markdown("-----")
    if button_needed:
        return button


page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
background-color: #0a0a0a;
opacity: 1;
background-image:  repeating-radial-gradient( circle at 0 0, transparent 0, #0a0a0a 40px ), 
repeating-linear-gradient( #5e5e5e55, #5e5e5e );
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

language_dictionary = get_language_codes()
selection_list = list(language_dictionary.keys())
selection_list.insert(0, "")

st.title("Language Flashcards")

if "reveal" not in st.session_state:
    st.session_state["reveal"] = False
if "generated" not in st.session_state:
    st.session_state["generated"] = False


language = st.selectbox("Select language", selection_list, disabled=True if st.session_state["generated"] else False)

if language != "":
    word = get_random_word()
    translation = translate(language_dictionary[language][1], word)
    while word.lower() == translation.lower():
        word = get_random_word()
        translation = translate(language_dictionary[language][1], word)

    if 'word' not in st.session_state:
        st.session_state["word"] = word.capitalize()
    if "translation" not in st.session_state:
        st.session_state["translation"] = translation

    if st.session_state["reveal"]:
        show_word_or_translation(st.session_state["word"])
        next_button = st.button("NEXT")

        if st.session_state["generated"]:
            st.session_state["generated"] = False
            st.experimental_rerun()

        if next_button:
            del st.session_state["word"]
            del st.session_state["translation"]
            st.session_state["reveal"] = False
            st.experimental_rerun()

    else:
        pronounce_button = show_word_or_translation(st.session_state["translation"], True)
        reveal_button = st.button("REVEAL")

        if not st.session_state["generated"]:
            st.session_state["generated"] = True
            st.experimental_rerun()

        if pronounce_button:
            get_speech(language_dictionary[language][0], st.session_state["translation"])

        if reveal_button:
            st.session_state["reveal"] = True
            st.experimental_rerun()
