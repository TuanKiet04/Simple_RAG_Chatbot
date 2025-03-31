import requests

BACKEND_URL = "http://127.0.0.1:8000"

def get_chat_history():
    try:
        response = requests.get(f"{BACKEND_URL}/history", timeout=5)
        response.raise_for_status()  # Gây lỗi nếu HTTP status không phải 200

        data = response.json()
        return data.get("history", []) if isinstance(data, dict) else data if isinstance(data, list) else []
    
    except requests.exceptions.RequestException as e:
        print(f"API request failed: {e}")
    except ValueError:
        print("Failed to parse JSON. Response:", response.text)
    
    return []
