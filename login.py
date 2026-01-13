import streamlit as st
import openai


openai.api_key = "YOUR_OPENAI_API_KEY"

st.title("🤖 AI Chat Bot (New API)")

if "messages" not in st.session_state:
    st.session_state.messages = []

msg = st.text_input("Your question")

if st.button("Send") and msg:
    st.session_state.messages.append(f"You: {msg}")
    
  
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": msg}]
    )
    
    answer = response.choices[0].message.content.strip()
    st.session_state.messages.append(f"Bot: {answer}")

 
for m in st.session_state.messages:
    st.write(m)


import streamlit as st
import openai
from datetime import datetime


openai.api_key = "YOUR_OPENAI_API_KEY"  # <-- Replace with your API key


st.set_page_config(page_title="AI Chat Bot", page_icon="🤖")

st.title("🤖 AI Chat Bot (Merged + Extendable)")


if "messages" not in st.session_state:
    st.session_state.messages = []

 
msg = st.text_input("Your question here:")

 
col1, col2 = st.columns([1,1])
with col1:
    send_btn = st.button("Send")
with col2:
    clear_btn = st.button("Clear Chat")

if clear_btn:
    st.session_state.messages = []
 
if send_btn and msg:
    st.session_state.messages.append(f"You: {msg}")

    try:
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": msg}]
        )
        answer = response.choices[0].message.content.strip()
    except Exception as e:
        answer = f"❌ Error: {e}"


    st.session_state.messages.append(f"Bot: {answer}")

 
    with open("chat_history.txt", "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} | You: {msg}\n")
        f.write(f"{datetime.now()} | Bot: {answer}\n")
        f.write("-"*50 + "\n")
 
for chat in st.session_state.messages:
    if chat.startswith("Bot:"):
        st.markdown(f"<div style='background-color:#E6E6FA; padding:10px; border-radius:10px; margin:5px 0'><b>Bot</b> [{datetime.now().strftime('%H:%M:%S')}]:<br>{chat[5:].strip()}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div style='background-color:#D1FFD1; padding:10px; border-radius:10px; margin:5px 0'><b>You</b> [{datetime.now().strftime('%H:%M:%S')}]:<br>{chat[5:].strip()}</div>", unsafe_allow_html=True)


import streamlit as st
import openai
from datetime import datetime

openai.api_key = "YOUR_OPENAI_API_KEY"  # <-- Replace with your key

st.set_page_config(page_title="AI Chat Bot", page_icon="🤖")

st.title("🤖 AI Chat Bot (Upgraded + Extendable)")

if "messages" not in st.session_state:
    st.session_state.messages = []

msg = st.text_input("Your question here:")


col1, col2 = st.columns([1, 1])
with col1:
    send_btn = st.button("Send")
with col2:
    clear_btn = st.button("Clear Chat")


if clear_btn:
    st.session_state.messages = []

if send_btn and msg:
    st.session_state.messages.append({
        "sender": "You",
        "message": msg,
        "time": datetime.now().strftime("%H:%M:%S")
    })

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": msg}]
        )
        answer = response.choices[0].message.content.strip()
    except Exception as e:
        answer = f"❌ Error: {e}"


    st.session_state.messages.append({
        "sender": "Bot",
        "message": answer,
        "time": datetime.now().strftime("%H:%M:%S")
    })


    with open("chat_history.txt", "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} | You: {msg}\n")
        f.write(f"{datetime.now()} | Bot: {answer}\n")
        f.write("-"*50 + "\n")


for chat in st.session_state.messages:
    if chat["sender"] == "Bot":
        st.markdown(
            f"<div style='background-color:#E6E6FA; padding:10px; border-radius:10px; margin:5px 0'>"
            f"<b>{chat['sender']}</b> [{chat['time']}]:<br>{chat['message']}</div>",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"<div style='background-color:#D1FFD1; padding:10px; border-radius:10px; margin:5px 0'>"
            f"<b>{chat['sender']}</b> [{chat['time']}]:<br>{chat['message']}</div>",
            unsafe_allow_html=True
        )


import streamlit as st

def show():
    st.header("Welcome to AI Chat Board!")
    st.write("""
        This is a fully-featured AI Chat Board built with Streamlit and OpenAI API.
        Use the sidebar to navigate:
        - Login
        - Chat
        - Settings
        - Feedback
        - About
    """)


import streamlit as st

def show():
    st.header("Login Page")
    
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    
    if st.session_state.logged_in:
        st.success("You are already logged in!")
        return
    
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        # Simple check for demonstration (hardcoded)
        if username == "user" and password == "1234":
            st.session_state.logged_in = True
            st.success(f"Welcome {username}!")
        else:
            st.error("Incorrect username or password")


import streamlit as st
import openai
from datetime import datetime


openai.api_key = "YOUR_OPENAI_API_KEY"  # <-- Replace your API key

def show():
    st.header("AI Chat Board")
    
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    msg = st.text_input("Type your message:")
    
    col1, col2 = st.columns([1,1])
    with col1:
        send_btn = st.button("Send")
    with col2:
        clear_btn = st.button("Clear Chat")
    
    if clear_btn:
        st.session_state.messages = []
    
    if send_btn and msg:
        # Save user message
        st.session_state.messages.append({
            "sender": "You",
            "message": msg,
            "time": datetime.now().strftime("%H:%M:%S")
        })
        
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": msg}]
            )
            answer = response.choices[0].message.content.strip()
        except Exception as e:
            answer = f"❌ Error: {e}"
        
        # Save bot message
        st.session_state.messages.append({
            "sender": "Bot",
            "message": answer,
            "time": datetime.now().strftime("%H:%M:%S")
        })
        
        # Save chat to file
  
    
    # Display chat
    for chat in st.session_state.messages:
        if chat["sender"] == "Bot":
            st.markdown(
                f"<div style='background-color:#E6E6FA; padding:10px; border-radius:10px; margin:5px 0'>"
                f"<b>{chat['sender']}</b> [{chat['time']}]:<br>{chat['message']}</div>",
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f"<div style='background-color:#D1FFD1; padding:10px; border-radius:10px; margin:5px 0'>"
                f"<b>{chat['sender']}</b> [{chat['time']}]:<br>{chat['message']}</div>",
                unsafe_allow_html=True
            )
