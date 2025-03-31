from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import logging
from database import init_db, save_message, get_chat_history

app = FastAPI()

# Cấu hình logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Khởi tạo database khi server chạy
init_db()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    logger.info("Client connected to WebSocket")
    try:
        while True:
            message = await websocket.receive_text()
            logger.info(f"Received message: {message}")
            
            save_message("user", message)  # Lưu tin nhắn người dùng
            response = f"Bot: You said '{message}'"
            save_message("assistant", response)  # Lưu phản hồi chatbot
            
            await websocket.send_text(response)
    except WebSocketDisconnect:
        logger.info("Client disconnected from WebSocket")
    except Exception as e:
        logger.error(f"WebSocket error: {e}")

@app.get("/history")
async def get_history():
    """ API lấy lịch sử chat """
    try:
        history = get_chat_history()
        return {"history": history}
    except Exception as e:
        logger.error(f"Error fetching chat history: {e}")
        return {"error": "Failed to retrieve chat history"}
