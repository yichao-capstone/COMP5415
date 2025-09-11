'''Comparison between Streamlit and HTML/CSS/JS'''
import streamlit as st

col1, col2 = st.columns(2)
with col1:
    with st.echo():
        st.markdown('''# :rainbow[Hello World!]''')
with col2:
    with st.echo():
        st.markdown('''<span style="background:\
                linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);
                -webkit-background-clip: text;
                color: transparent;
                font-size: 3em;
                font-weight: bold;">
                Hello World!
                </span>''',
                unsafe_allow_html=True)
