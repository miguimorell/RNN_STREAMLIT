import streamlit as st
from save_melody2 import save_melody2
from create_checkbox import create_checkbox
from insert_temperature import insert_temperature
from check_checkbox import check_checkbox
from call_api import call_api


url_logo ='https://st2.depositphotos.com/15317184/46760/v/600/depositphotos_467603324-stock-illustration-p-letter-logo-letter-p.jpg'

# Mostrar logo
st.image(url_logo, width=600)


col1,col2=st.columns([4,6])

with col1:
    # Mostrar un GIF desde una URL
    url_gif = 'https://media2.giphy.com/media/xRYN8w3CKPcv6/giphy.gif?cid=ecf05e47ataqoy877rlderctx8xbcb7mqzsgi8tm8r3ginfd&ep=v1_gifs_search&rid=giphy.gif&ct=g'

    # Mostrar el GIF con un tamaño reducido
    st.image(url_gif, width=250)


with col2:
    # Texto más pequeño con estilo personalizado
    st.markdown("""
    <div style='font-size: 23px; width: 400px; height: 80px; display: flex; align-items: center; justify-content: center; text-align: center; border: 1px solid black;'>
        <b>Need some inspiration for your music creation?</b>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div style='font-size: 23px; width: 400px; height: 80px; display: flex; align-items: center; justify-content: center; text-align: center; border: 1px solid black;'>
            <b>Need a companion to spice up your drum grooves?</b>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
        <div style='font-size: 23px; width: 400px; height: 80px; display: flex; align-items: center; justify-content: center; text-align: center; border: 1px solid black;'>
            <b>Sick of your current bass player and want to look for a replacement?</b>
        </div>
        """, unsafe_allow_html=True)





#List of sounds, block of boxes for the two groups of 16th notes.
sounds_first_block = create_checkbox("Enter the drums for the first bar:","1")
st.write("---")
sounds_second_block = create_checkbox("Enter the drums for the second bar:","2")
st.write("---")
#Botton to specify temperature
st.session_state['temperature']=insert_temperature()
st.write("---")

title = st.text_input('Insert File Name', 'Bass')

# Botón Submit
if st.button("Create Bass Sound"):

    # Almacenar los resultados seleccionados en una lista
    # Primer bloque de cajas
    kick_data,snare_data,charles_data = check_checkbox(sounds_first_block)

    # Segundo bloque de cajas
    kick_data2,snare_data2,charles_data2 = check_checkbox(sounds_second_block)

    #Concatenar los outputs en 3 strings.
    #orden-> Charles, kick, snare
    #Sumar las listas de los dos bloques

    kick=kick_data+kick_data2
    snare=snare_data+snare_data2
    charles=charles_data+charles_data2

    st.session_state['kick'] = kick
    st.session_state['snare'] = snare
    st.session_state['charles'] = charles

    kick_str = ",".join(str(elemento) for elemento in kick)
    snare_str = ",".join(str(elemento) for elemento in snare)
    charles_str = ",".join(str(elemento) for elemento in charles)

    #call api
    query = call_api(charles_str,kick_str,snare_str,st.session_state["temperature"])

    bass=[]
    for key, value in query.items():
        bass.append(value)

    # Save the melody as a MIDI file
    file_name = title+'.mid'
    save_melody2(bass, step_duration=0.25,format='midi', file_name= file_name)

    # Provide download link for the generated MIDI file
    audio_file = open(file_name, 'rb')
    audio_bytes = audio_file.read()
    st.download_button("Download MIDI File", data=audio_bytes, file_name=file_name)
