import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect('chat_history.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS chat_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            role TEXT NOT NULL,
            content TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()

import html

def save_message(role, content):
    conn = sqlite3.connect('chat_history.db')
    cursor = conn.cursor()
    
    # Clean content based on role
    if role == 'user':
        # Remove HTML tags for user messages
        content = content.replace('<p>', '').replace('</p>', '').strip()
    
    cursor.execute('''
        INSERT INTO chat_history (role, content)
        VALUES (?, ?)
    ''', (role, content))
    
    conn.commit()
    conn.close()

def get_all_messages():
    conn = sqlite3.connect('chat_history.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT role, content FROM chat_history ORDER BY timestamp')
    messages = cursor.fetchall()
    
    conn.close()
    
    # Convert to list of dictionaries for better handling
    return [{'role': role, 'content': content} for role, content in messages]

def clear_history():
    conn = sqlite3.connect('chat_history.db')
    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM chat_history')
    conn.commit()
    conn.close()
