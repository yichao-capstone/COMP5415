import streamlit as st

if 'messages' not in st.session_state:
        st.session_state['messages'] = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"]) 

if prompt := st.chat_input("What do you want to discuss?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

if st.button("Clear Discussion"):
    st.session_state['messages'] = []