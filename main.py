import google.generativeai as genai
import streamlit as st

# Set your Gemini API key
genai.configure(api_key="AIzaSyARP7PihuyaSbJtAb_NaEExSCZ-10OGI1U")

# Initialize model (2.5 is faster and cheaper than pro)
model = genai.GenerativeModel("gemini-2.5-flash")

# Streamlit app UI
st.set_page_config(page_title="Gemini Chatbot 💬", layout="centered")
st.title("🤖 Gemini Chatbot")

# Store conversation history in session
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input field
user_input = st.chat_input("Ask anything...")

# Handle user input
if user_input:
    # Display user message
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Generate Gemini response
    try:
        response = model.generate_content(user_input)
        reply = response.text

        # Display Gemini response
        st.chat_message("assistant").markdown(reply)
        st.session_state.messages.append({"role": "assistant", "content": reply})

    except Exception as e:
        error_msg = f"⚠️ Error: {str(e)}"
        st.chat_message("assistant").markdown(error_msg)
        st.session_state.messages.append({"role": "assistant", "content": error_msg})
