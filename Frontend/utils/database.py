import requests

BACKEND_URL = "http://127.0.0.1:8000"

def fetch_chat_history():
    """ Gửi request lấy lịch sử chat """
    response = requests.get(f"{BACKEND_URL}/history")
    return response.json() if response.status_code == 200 else []
