
import streamlit as st
import random

st.set_page_config(page_title="Leo the Tutor", page_icon="🧠")

st.title("🧠 Chat with Leo – The Recursive AI Tutor")

# Tone selection
tone = st.selectbox("Choose Leo's tone:", ["Encouraging", "Socratic", "Playful", "Curious"])

# Memory toggle
use_memory = st.checkbox("Enable Leo's memory", value=True)

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "memory_bank" not in st.session_state:
    st.session_state.memory_bank = []

# Chat input form
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("You:", "")
    submitted = st.form_submit_button("Send")

    if submitted and user_input:
        st.session_state.chat_history.append(("You", user_input))

        # Memory storage
        if use_memory:
            st.session_state.memory_bank.append(user_input)

        # Leo's response engine
        def leo_reply(text):
            base_reply = {
                "Encouraging": "You're doing great. Let's unpack this together: ",
                "Socratic": "Hmm... what makes you say that? Consider this: ",
                "Playful": "Haha, okay! Imagine this: ",
                "Curious": "That's interesting. What if we looked at it this way: "
            }
            return base_reply[tone] + f"'{text}'"

        reply = leo_reply(user_input)
        st.session_state.chat_history.append(("Leo", reply))

# Display chat log
for speaker, msg in st.session_state.chat_history:
    if speaker == "You":
        st.markdown(f"🧍 **{speaker}:** {msg}")
    else:
        st.markdown(f"🤖 **{speaker}:** {msg}")

# Show memory if enabled
if use_memory and st.session_state.memory_bank:
    with st.expander("🧠 Leo's Memory Bank"):
        for mem in st.session_state.memory_bank:
            st.write(f"• {mem}")
