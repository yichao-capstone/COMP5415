import streamlit as st
import random
import time
with st.echo():
    numbers = list(range(1, 7))
    def startTheGame(nmb):
        random.shuffle(nmb)
        for n in nmb:
            yield n
            time.sleep(1)
    if st.button("Roll"):
        

        st.write_stream(startTheGame(numbers))