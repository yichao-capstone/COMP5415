'''Comparison between Streamlit and HTML/CSS/JS'''
import streamlit as st

col1, col2 = st.columns(2)
with col1:
    with st.echo():
        st.markdown("st.markdown(css + '<div class=\"rainbow\">Hello World!</div>', unsafe_allow_html=True)")
with col2:
    css = """
    <style>
    .rainbow {
      font-size: 4rem;
      font-weight: 800;
      background: linear-gradient(90deg, red, orange, yellow, green, blue, indigo, violet);
      background-size: 400%;
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      animation: rainbow 5s linear infinite;
      text-align: center;
      margin: 1rem 0;
    }
    @keyframes rainbow {
      0% { background-position: 0% 50%; }
      50% { background-position: 100% 50%; }
      100% { background-position: 0% 50%; }
    }
    </style>
    """
    st.markdown(css + '<div class="rainbow">Hello World!</div>', unsafe_allow_html=True)
