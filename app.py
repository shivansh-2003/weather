import openai
import streamlit as st

# Directly set your OpenAI API key here
openai.api_key = ""
if 'messages' not in st.session_state:
    st.session_state.messages = []

def generate_response(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=300,
        temperature=0.7
    )
    return response.choices[0].message['content'].strip()

def clear_chat():
    st.session_state.messages = []

def main():
    st.set_page_config(page_title="Climate Change Awareness Bot", page_icon="🌍")

    # Header
    st.markdown("<h1 style='text-align: center; color: green;'>Climate Change Awareness Bot 🌍</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: grey;'>Ask about climate data, carbon footprint tips, or awareness content!</p>", unsafe_allow_html=True)

    # Chat input
    user_input = st.text_input("Your question:")

    if st.button("Ask"):
        if user_input:
            # Append user input to chat history
            st.session_state.messages.append({"role": "user", "content": user_input})

            # Generate response from GPT-3.5 Turbo
            response = generate_response(st.session_state.messages)

            # Append bot response to chat history
            st.session_state.messages.append({"role": "assistant", "content": response})

    # Display the conversation
    for message in st.session_state.messages:
        if message['role'] == 'user':
            st.markdown(f"<div style='background-color: #DCF8C6; padding: 10px; border-radius: 5px; margin-bottom: 10px;'>**You:** {message['content']}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div style='background-color: #F1F0F0; padding: 10px; border-radius: 5px; margin-bottom: 10px;'>**Bot:** {message['content']}</div>", unsafe_allow_html=True)

    # Clear chat button
    if st.button("Clear Chat"):
        clear_chat()

if __name__ == "__main__":
    main()
