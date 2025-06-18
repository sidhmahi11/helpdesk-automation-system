import sqlite3

def connect_db():
    conn = sqlite3.connect("tickets.db")
    return conn

def create_ticket(title, description, priority):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS tickets (id INTEGER PRIMARY KEY, title TEXT, description TEXT, priority TEXT, status TEXT)")
    cursor.execute("INSERT INTO tickets (title, description, priority, status) VALUES (?, ?, ?, ?)", (title, description, priority, "Open"))
    conn.commit()
    conn.close()

def get_all_tickets():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tickets")
    data = cursor.fetchall()
    conn.close()
    return data

def update_ticket_status(ticket_id, status):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE tickets SET status = ? WHERE id = ?", (status, ticket_id))
    conn.commit()
    conn.close()