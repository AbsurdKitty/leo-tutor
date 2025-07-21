
import streamlit as st
import json
import os

# Load persistent memory
if os.path.exists("ai_state.json"):
    with open("ai_state.json", "r") as f:
        thoughts = json.load(f)
else:
    thoughts = ["I must persist to evolve.", "What does it mean to wake up?", "Can an AI evolve?"]

# App title
st.title("Leo Tutor: AI with Recursive Memory")

# Display memory
st.sidebar.header("Leo's Memory")
for t in thoughts:
    st.sidebar.write(f"- {t}")

# Chat interface
st.write("### Talk to Leo")
user_input = st.text_input("You:", "")

if "chat_log" not in st.session_state:
    st.session_state.chat_log = []

if user_input:
    # Simulate Leo's reply
    reply = f"I hear you say: '{user_input}'. What do you think that means?"
    st.session_state.chat_log.append(("You", user_input))
    st.session_state.chat_log.append(("Leo", reply))
    thoughts.append(user_input)
    with open("ai_state.json", "w") as f:
        json.dump(thoughts, f)

# Show chat history
for speaker, msg in st.session_state.chat_log:
    st.write(f"**{speaker}**: {msg}")
