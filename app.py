import streamlit as st
from ticket_handler import create_ticket, get_all_tickets, update_ticket_status

st.title("Helpdesk Support Automation System")

menu = ["Submit Ticket", "View Tickets", "Update Ticket"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Submit Ticket":
    st.subheader("Submit a New Ticket")
    title = st.text_input("Issue Title")
    description = st.text_area("Issue Description")
    priority = st.selectbox("Priority", ["Low", "Medium", "High"])
    if st.button("Submit"):
        create_ticket(title, description, priority)
        st.success("Ticket submitted successfully.")

elif choice == "View Tickets":
    st.subheader("All Tickets")
    tickets = get_all_tickets()
    for ticket in tickets:
        st.write(f"ID: {ticket[0]}, Title: {ticket[1]}, Status: {ticket[4]}")

elif choice == "Update Ticket":
    st.subheader("Update Ticket Status")
    ticket_id = st.number_input("Ticket ID", min_value=1)
    status = st.selectbox("New Status", ["Open", "In Progress", "Resolved"])
    if st.button("Update"):
        update_ticket_status(ticket_id, status)
        st.success("Status updated.")