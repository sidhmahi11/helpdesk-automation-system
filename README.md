# Helpdesk Support Automation System 🛠️

A web-based IT support ticketing system built using Python and Streamlit. The project simulates real-world ITSM workflows like ticket creation, status tracking, and SLA management.

---

## 🔍 Features
- 🎫 Submit new helpdesk tickets with title, description, and priority
- 📊 View and manage all submitted tickets
- 🔄 Update ticket statuses (Open → In Progress → Resolved)
- 💾 Local storage with SQLite for persistence
- 🧠 Simulates basic ITSM functionality for IT Analyst/Support scenarios

---

## 🚀 Live Demo

👉 [Click to View App](https://sidhmahi11-helpdesk-automation-system-app-na2771.streamlit.app)

---

## 🖼️ Demo Screenshot

[!Submit_Ticket]![Screenshot 2025-06-18 204341](https://github.com/user-attachments/assets/e004bb11-04c6-46f1-bdc8-29feb9298d0a)
[!View Ticket]![Screenshot 2025-06-18 204433](https://github.com/user-attachments/assets/27cb50a3-2c48-4cf2-8a89-1ace61012a69)
[!Update_Ticket]![Screenshot 2025-06-18 204418](https://github.com/user-attachments/assets/4a9194d4-6f16-4814-bd05-735c74e32a70)

---

## 🧰 Tech Stack
- Python
- Streamlit
- SQLite
- GitHub
- Deployed on [Streamlit Cloud](https://streamlit.io/cloud)

---

## 📁 Folder Structure
```
helpdesk-automation-system/
├── app.py                # Main Streamlit interface
├── ticket_handler.py     # Ticket logic (create, view, update)
├── requirements.txt      # Dependencies (streamlit only)
├── README.md             # Documentation
├── Demo Screenshot/      # UI snapshots
└── tickets.db            # SQLite file auto-created on first run
```

---

## ✨ Output Example

When a user submits a ticket:
- It is added to a SQLite database with **status: Open**
- Can be tracked in “View Tickets” tab
- Can be updated using Ticket ID to “In Progress” or “Resolved”

```
Ticket ID: 1
Title: Wi-Fi Not Working
Priority: High
Status: Open → In Progress → Resolved
```

---

## 🧑‍💻 Author
**Siddhant Jain**  
📧 siddhantjain261@gmail.com  
🔗 [GitHub](https://github.com/sidhmahi11/helpdesk-automation-system)

