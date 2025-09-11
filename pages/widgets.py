import streamlit as st

tab1, tab2, tab3 = st.tabs(["button", "slider", "checkbox"])
with tab1:
    with st.echo():
        st.title('button')
        if st.button("Click me", type='primary'):
            st.write("Clicked!")
with tab2:
    with st.echo():
        st.title('slider')
        age = st.slider("How old are you?", 0, 130, 25)
        st.write("I'm ", age, 'years old')
with tab3:
    with st.echo():
        st.title('checkbox')
        agree = st.checkbox('tick me')
        if agree:
            st.write('Ticked!')