import sqlite3

DB_FILE = "chat_history.db"

def init_db():
    """ Tạo database nếu chưa có """
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            role TEXT,
            content TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_message(role, content):
    """ Lưu tin nhắn vào database """
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("INSERT INTO messages (role, content) VALUES (?, ?)", (role, content))
    conn.commit()
    conn.close()
    
def get_messages():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT user, message, timestamp FROM messages ORDER BY timestamp ASC")
    messages = cursor.fetchall()
    conn.close()
    return messages

init_db()

def get_chat_history():
    """ Lấy toàn bộ lịch sử chat """
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT role, content FROM messages")
    messages = [{"role": row[0], "content": row[1]} for row in c.fetchall()]
    conn.close()
    return messages


