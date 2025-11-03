import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage
from chatbot.graph import send_message  # Replace with the actual filename (without .py)

st.set_page_config(page_title="Wisdom", page_icon="🤖")

st.image("logo.png", width=75)
st.title("Wisdom - AI knowledge base",)

# Session state for chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []
if "thread_id" not in st.session_state:
    st.session_state["thread_id"] = "central-memories"  # Replace with unique user id if needed

# Display chat history
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.markdown(msg.content)
    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(msg.content)

# Chat input
if prompt := st.chat_input("Type your message..."):
    # Add user message to session
    human_msg = HumanMessage(content=prompt)
    st.session_state.messages.append(human_msg)

    # Display immediately
    with st.chat_message("user"):
        st.markdown(prompt)

    # Send message to backend
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response_text = send_message(
                    thread_id=st.session_state.thread_id,
                    user_message=prompt
                )
                ai_msg = AIMessage(content=response_text)
                st.session_state.messages.append(ai_msg)
                st.markdown(response_text)
            except Exception as e:
                st.error(f"Error: {e}")
