import sqlite3
import pandas as pd

def init_db():
    conn = sqlite3.connect('study_tracker.db')
    c = conn.cursor()
    # Users table
    c.execute('''CREATE TABLE IF NOT EXISTS users 
                 (username TEXT PRIMARY KEY, password TEXT)''')
    # Study Logs
    c.execute('''CREATE TABLE IF NOT EXISTS study_logs 
                 (username TEXT, duration REAL, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
    # Friends
    c.execute('''CREATE TABLE IF NOT EXISTS friends 
                 (user1 TEXT, user2 TEXT)''')
    conn.commit()
    conn.close()

def log_study_time(username, hours):
    conn = sqlite3.connect('study_tracker.db')
    c = conn.cursor()
    c.execute("INSERT INTO study_logs (username, duration) VALUES (?, ?)", (username, hours))
    conn.commit()
    conn.close()
