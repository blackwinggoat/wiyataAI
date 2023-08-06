import openai
import streamlit as st

# Please replace 'your-api-key' with your actual OpenAI API key
openai.api_key = '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'

st.title("OpenAI Chatbot")

if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

if st.session_state["chat_history"]:
    for message in st.session_state["chat_history"]:
        if message["role"] == "system" or message["role"] == "assistant":
            st.write(f'AI: {message["content"]}')
        else:
            st.write(f'User: {message["content"]}')

user_input = st.text_input("Your Message:")
if st.button("Send"):
    if user_input:
        st.session_state["chat_history"].append({"role": "user", "content": user_input})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=st.session_state["chat_history"]
        )
        st.session_state["chat_history"].append(response.choices[0].message)
