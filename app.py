import streamlit as st
from agent import query_database_or_llm

# Set up page config and title
st.set_page_config(page_title="RDS Chatbot", layout="wide")
st.title("🤖 Chat with your RDS MySQL DB + General Knowledge")

# Sidebar control
st.sidebar.header("Control Panel")
if st.sidebar.button("Clear Chat"):
    st.session_state["history"] = []

# Session state initialization
if "history" not in st.session_state:
    st.session_state["history"] = []

# Input field
user_input = st.text_input("Ask your database or LLM anything:", key="input")

# Submit button
submit = st.button("Submit")

# Process input
if submit and user_input:
    with st.spinner("Thinking..."):
        response = query_database_or_llm(user_input)
        st.session_state["history"].append((user_input, response))
        st.markdown(f"**You:** {user_input}")
        st.markdown(f"**Bot:** {response}")

# Custom CSS for styling
st.markdown("""
    <style>
        .stTextInput>div>div>input {
            padding: 12px;
            font-size: 16px;
            border-radius: 8px;
        }
        .stButton>button {
            background-color: #0072C6;
            color: white;
            padding: 10px 20px;
            font-size: 16px;
            border: none;
            border-radius: 8px;
        }
        .stButton>button:hover {
            background-color: #005fa3;
        }
        .css-1d391kg {  /* Light background for response box */
            background-color: #f8f9fa;
            border-radius: 10px;
            padding: 10px;
        }
    </style>
""", unsafe_allow_html=True)
