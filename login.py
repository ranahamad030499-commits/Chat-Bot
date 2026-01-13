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
