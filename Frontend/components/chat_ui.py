import streamlit as st

def display_messages(messages):
    """ Hiển thị lịch sử tin nhắn với avatar """
    for msg in messages:
        avatar = "🧑" if msg["role"] == "user" else "🤖"
        with st.chat_message(msg["role"], avatar=avatar):
            st.markdown(msg["content"])