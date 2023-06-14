import streamlit as st


def insert_temperature():
    st.markdown("<span style='font-size:20px'><b>Temperature</b> is a parameter that adds randomness to the generation.<br><span style='font-size:16px'>Numbers closer to 0 make the model more deterministic.<br>Numbers closer to 1 make the generation more unpredictable.</span></span>", unsafe_allow_html=True)

    temperature = st.slider('Select a value for the temperature', 0.0, 1.0, step=0.1)

    return temperature
