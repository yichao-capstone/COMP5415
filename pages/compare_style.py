'''Comparison between Streamlit and HTML/CSS/JS'''
import streamlit as st
from pathlib import Path
import streamlit.components.v1 as components
css_text = Path('assets/ex.css').read_text()
html_body = '''<div id='ex'><span>Hello World!</span></div>'''
tab1, tab2 = st.tabs(["Example1", "Example2"])

with tab2:
    col1, col2 = st.columns(2,border=True)
    with col1:
        st.title("Streamlit with Markdown")
        with st.echo():
            st.markdown('''# :rainbow[Hello World!]''')
    with col2:
        css_rainbow = f'''<!doctype html>
            <html lang="en">
            <head>
            <style>{css_text}</style>
            <meta charset="utf-8">
            <title>Hello World</title>
            </head>
            <body>
            {html_body}
            </body>
            </html>'''
        st.title("HTML with CSS")
        debug = st.toggle("Show code in .css", value=True)
        if debug:
            st.code(css_text, line_numbers=True)
        st.code('''<!doctype html>
            <html lang="en">
            <head>
            <style>{css_text}</style>
            <meta charset="utf-8">
            <title>Hello World</title>
            </head>
            <body>
            {html_body}
            </body>
            </html>''', line_numbers=True)
        components.html(css_rainbow, height=100)
        
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
