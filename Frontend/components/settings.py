import streamlit as st

def apply_dark_mode():
    """ Áp dụng chế độ Dark Mode """
    st.markdown("""
        <style>
            body {background-color: #1e1e1e; color: white;}
            .stTextInput, .stTextArea {color: white !important;}
        </style>
    """, unsafe_allow_html=True)