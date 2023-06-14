import os
os.environ['SDL_AUDIODRIVER'] = 'directsound'

import streamlit as st
import music21 as m21
from save_melody2 import save_melody2
from create_checkbox import create_checkbox
from insert_temperature import insert_temperature
from check_checkbox import check_checkbox
from call_api import call_api

'''
# Grove-Nator 3000
'''

'''
## Tired of your friend not being able to play with you?....
## Do not worry, Grove-Nator3000 arrives to make your life easier...
'''


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
    stream=save_melody2(bass, step_duration=0.25,format='midi', file_name= file_name)
