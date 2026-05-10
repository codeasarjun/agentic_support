
import sqlite3

DB_NAME = "database/tickets.db"


def init_db():
    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tickets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ticket TEXT,
        category TEXT,
        sentiment TEXT,
        response TEXT,
        escalation TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_ticket(ticket, category, sentiment, response, escalation):
    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO tickets (
        ticket,
        category,
        sentiment,
        response,
        escalation
    )
    VALUES (?, ?, ?, ?, ?)
    """, (
        ticket,
        category,
        sentiment,
        response,
        escalation
    ))

    conn.commit()
    conn.close()