'''Comparison between Streamlit and HTML/CSS/JS'''
import streamlit as st
tab1, tab2 = st.tabs(["Example1", "Example2"])
with tab2:
    col1, col2 = st.columns(2,border=True)
    with col1:
        st.title("Streamlit with Markdown")
        with st.echo():
            st.markdown('''# :rainbow[Hello World!]''')
    with col2:
            css_rainbow = '''<span style="
                background: linear-gradient(to right, 
                    red, orange, yellow, green, blue, indigo, violet);
                -webkit-background-clip: text;
                color: transparent;
                font-size: 3em;
                font-weight: bold;">
                Hello World!
                </span>'''
            st.title("HTML with CSS")
            st.code(css_rainbow, line_numbers=True)
            st.markdown(css_rainbow,
                    unsafe_allow_html=True)
with tab1:
    col1, col2 = st.columns(2,border=True)
    with col1:
        with st.echo():
            st.title('Hello World!')
    with col2:
         html_hello = """
            <!doctype html>
            <html lang="en">
            <head>
            <meta charset="utf-8">
            <title>Hello World</title>
            </head>
            <body>
            <h1>Hello World!</h1>
            </body>
            </html>
            """
         st.code(html_hello, line_numbers=True)
         st.markdown(html_hello, unsafe_allow_html=True)