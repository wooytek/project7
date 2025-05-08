import streamlit as st
from agent import get_sql_agent

# Set up page config and title
st.set_page_config(page_title="RDS Chatbot", layout="wide")
st.title("🤖 Chat with your RDS MySQL DB")

# Initialize the session state for history if not already set
if "history" not in st.session_state:
    st.session_state["history"] = []

# Sidebar for controls
st.sidebar.header("Control Panel")
clear_history = st.sidebar.button("Clear History")

if clear_history:
    st.session_state["history"] = []  # Reset history

# Initialize agent
agent = get_sql_agent()

# User input field and submit button
user_input = st.text_input("Ask your database anything:", key="user_input")

# Displaying the conversation
if user_input:
    submit_button = st.button("Submit")
    if submit_button:
        with st.spinner("Thinking..."):
            response = agent.run(user_input)
            st.session_state["history"].append(("You", user_input))
            st.session_state["history"].append(("Bot", response))

# Display the conversation history
if len(st.session_state["history"]) > 0:
    st.markdown("### Conversation History:")
    for idx in range(len(st.session_state["history"]) - 1, -1, -2):
        if idx > 0:
            user_msg = st.session_state["history"][idx - 1][1]
            bot_msg = st.session_state["history"][idx][1]
            st.markdown(f"**You:** {user_msg}")
            st.markdown(f"**Bot:** {bot_msg}")

# Styling (Custom CSS)
st.markdown("""
    <style>
        .css-1d391kg {
            background-color: #f1f1f1;
            border-radius: 8px;
            padding: 10px;
            font-family: 'Arial', sans-serif;
        }
        .stTextInput>div>div>input {
            padding: 10px;
            font-size: 14px;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            border-radius: 5px;
            padding: 10px 15px;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
    </style>
""", unsafe_allow_html=True)
