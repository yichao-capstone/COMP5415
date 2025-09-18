import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt 

max_words = 15
if 'messages1' not in st.session_state:
        st.session_state['messages1'] = []
        st.session_state['messages2'] = []
        st.session_state['messages3'] = []

# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"]) 
tb1,tb2,tb3=st.tabs(["Yichao","Lin","Yuan"])
with tb1:
   
    for message in st.session_state.messages1:
        with st.chat_message(message["role"]):
            st.markdown(message["content"]) 
    if prompt := st.chat_input("What do you want to discuss?",key="input1"):
        st.session_state.messages1.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
    text=''
    for rcd in st.session_state['messages1']:
        text=text+rcd['content']
    if st.button("Generate Word Cloud",key='b1') and text:
        wordcloud = WordCloud(
            width=800,
            height=400,
            max_words=max_words,
        ).generate(text)

    # Show word cloud
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.axis("off")
        st.pyplot(fig)
    if st.button("Clear Discussion",key='c1'):
        st.session_state['messages1'] = []
with tb2:
    for message in st.session_state.messages2:
        with st.chat_message(message["role"]):
            st.markdown(message["content"]) 
    if prompt := st.chat_input("What do you want to discuss?",key="input2"):
        st.session_state.messages2.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
    text=''
    for rcd in st.session_state['messages2']:
        text=text+rcd['content']
    if st.button("Generate Word Cloud",key='b2') and text:
        wordcloud = WordCloud(
            width=800,
            height=400,
            max_words=max_words,
        ).generate(text)
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.axis("off")
        st.pyplot(fig)
    if st.button("Clear Discussion",key='c2'):
        st.session_state['messages2'] = []
with tb3:
    for message in st.session_state.messages3:
        with st.chat_message(message["role"]):
            st.markdown(message["content"]) 
    if prompt := st.chat_input("What do you want to discuss?",key="input3"):
        st.session_state.messages3.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
    text=''
    for rcd in st.session_state['messages3']:
        text=text+rcd['content']
    if st.button("Generate Word Cloud",key='b3') and text:
        wordcloud = WordCloud(
            width=800,
            height=400,
            max_words=max_words,
        ).generate(text)
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.axis("off")
        st.pyplot(fig)
    if st.button("Clear Discussion",key='c3'):
        st.session_state['messages3'] = []
