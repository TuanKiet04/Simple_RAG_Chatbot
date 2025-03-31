import websocket as ws

def connect_ws():
    """ Tạo kết nối WebSocket """
    return ws.create_connection("ws://127.0.0.1:8000/ws")

cli = ws.WebSocket()
cli.connect("ws://127.0.0.1:8000/ws")
cli.send("Hello, server!")
response = cli.recv()
print(f"Response from server: {response}")
cli.close()