import streamlit as st
import time
import websockets
import asyncio
from components.chat_ui import display_messages
from components.settings import apply_dark_mode
from utils.ws_client import connect_ws
from utils.api import get_chat_history
from utils.database import fetch_chat_history  

# Cấu hình trang
st.set_page_config(page_title="Low-Code Chatbot", layout="wide")

# Áp dụng Dark Mode
apply_dark_mode()

st.markdown("<h2 style='text-align: center;'>💬 Low-Code Chatbot</h2>", unsafe_allow_html=True)

# Kết nối WebSocket
ws = connect_ws()

# Hiển thị lịch sử tin nhắn
st.subheader("Chat History")
chat_history = get_chat_history()

for entry in chat_history:
    role = entry.get("role", "unknown")
    content = entry.get("content", "")
    st.text(f"{role}: {content}")

st.subheader("Chat with Bot")

# Nút xóa lịch sử chat
if st.button("Clear Chat"):
    st.session_state.messages = []
    st.rerun()

# Hàm gửi tin nhắn qua WebSocket
async def send_message(ws, message):
    await ws.send(message)
    return await ws.recv()

# Lấy lịch sử chat từ database
if "messages" not in st.session_state:
    st.session_state.messages = fetch_chat_history()

# Hiển thị tin nhắn
display_messages(st.session_state.messages)

# Nhập tin nhắn
user_input = st.chat_input("Type your message here...")

if user_input:
    # Lưu & hiển thị tin nhắn người dùng
    st.session_state.messages.append({"role": "user", "content": user_input})
    display_messages([{"role": "user", "content": user_input}])

    # Hiển thị hiệu ứng typing
    with st.chat_message("assistant", avatar="🤖"):
        typing_placeholder = st.empty()
        typing_placeholder.markdown("🤖 *Chatbot is typing...*")
        time.sleep(1.5)

    # Gửi tin nhắn & nhận phản hồi
    response = asyncio.run(send_message(ws, user_input))

    # Xóa hiệu ứng typing và hiển thị phản hồi chatbot
    typing_placeholder.empty()
    st.session_state.messages.append({"role": "assistant", "content": response})
    display_messages([{"role": "assistant", "content": response}])
