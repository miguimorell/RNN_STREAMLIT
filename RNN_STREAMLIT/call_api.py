import requests
import streamlit as st

def call_api(charles_str,kick_str,snare_str,temperature):
#orden-> Charles, kick, snare
    #api:
    #url="http://127.0.0.1:8000/predict"
    url="https://rnnmusicgenerator-pdjk6hbk2a-ew.a.run.app/predict"
    params={"CH":charles_str,"CK":kick_str,"SN":snare_str,"T":temperature}

    with st.spinner('Composing Bass Sound...'):
        query=requests.get(url,params).json()
    st.success('Done!')

    return query
