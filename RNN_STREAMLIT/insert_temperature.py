import streamlit as st


def insert_temperature():
    st.write("¨**Temperature**¨ is a parameter that adds randomness to the generation: Numbers closer to 0 make the model more deterministic. Numbers closer to 1 makes the generation more unpredictable.")
    temperature = st.slider('Select a value for the temperature', 0.0, 1.0, step=0.1)

    return temperature
