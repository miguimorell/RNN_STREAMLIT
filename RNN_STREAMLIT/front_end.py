import streamlit as st
from save_melody2 import save_melody2
from create_checkbox import create_checkbox
from insert_temperature import insert_temperature
from check_checkbox import check_checkbox
from call_api import call_api
from generate_drum_midi import generate_drum_midi




######################################################################
#initialize variables

if "Download" not in st.session_state:
    st.session_state["Download"] = True

if "Download_press" not in st.session_state:
    st.session_state["Download_press"] = False

if "Download_charles" not in st.session_state:
    st.session_state["Download_charles"] = True

if "Download_press_charles" not in st.session_state:
    st.session_state["Download_press_charles"] = False

if "Download_kick" not in st.session_state:
    st.session_state["Download_kick"] = True

if "Download_press_kick" not in st.session_state:
    st.session_state["Download_press_kick"] = False

if "Download_snare" not in st.session_state:
    st.session_state["Download_snare"] = True

if "Download_press_snare" not in st.session_state:
    st.session_state["Download_press_snare"] = False
######################################################################

# Mostrar logo

url_logo ='https://i.imgur.com/IZxZVtm.png'
st.image(url_logo, width=670)

col1,col2=st.columns([4,6])

with col1:
    # Mostrar un GIF desde una URL
    url_gif = 'https://media2.giphy.com/media/xRYN8w3CKPcv6/giphy.gif?cid=ecf05e47ataqoy877rlderctx8xbcb7mqzsgi8tm8r3ginfd&ep=v1_gifs_search&rid=giphy.gif&ct=g'

    # Mostrar el GIF con un tamaño reducido
    st.image(url_gif, width=250)


with col2:
    # Texto más pequeño con estilo personalizado
    st.markdown("""
    <div style='font-size: 23px; width: 400px; height: 81px; display: flex; align-items: center; justify-content: center; text-align: center; border: 0px solid black;'>
        <b>Need some inspiration for your music creation?</b>
    </div>
    """, unsafe_allow_html=True)


    st.markdown("""
        <div style='font-size: 23px; width: 400px; height: 81px; display: flex; align-items: center; justify-content: center; text-align: center; border-top: 2px solid black; border-bottom: 2px solid black;'>
            <b>Need a companion to spice up your drum grooves?</b>
        </div>
        """, unsafe_allow_html=True)


    st.markdown("""
        <div style='font-size: 23px; width: 400px; height: 81px; display: flex; align-items: center; justify-content: center; text-align: center; border: 0px solid black;'>
            <b>Sick of your current bass player and want to look for a replacement?</b>
        </div>
        """, unsafe_allow_html=True)
######################################################################

#List of sounds, block of boxes for the two groups of 16th notes.

sounds_first_block = create_checkbox("**Enter the drums for the first bar:**", "1")
st.write("---")

sounds_second_block = create_checkbox("**Enter the drums for the second bar:**","2")
st.write("---")

######################################################################

#Botton to specify temperature
st.session_state['temperature']=insert_temperature()
st.write("---")

######################################################################
#Name for Bass midi file
title = st.text_input('Insert File Name for the File to be Downloaded', 'Bass')

######################################################################

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

    # #generate drums sound as midi
    generate_drum_midi(charles_str,kick_str,snare_str)

    #call api
    query = call_api(charles_str,kick_str,snare_str,st.session_state["temperature"])

    bass=[]
    for key, value in query.items():
        bass.append(value)

    # Save the melody as a MIDI file
    st.session_state["file_name"] = title+'.mid'
    save_melody2(bass, step_duration=0.25,format='midi', file_name= st.session_state["file_name"])

    # Provide download link for the generated MIDI file
    audio_file = open(st.session_state["file_name"], 'rb')
    st.session_state["audio_bytes"] = audio_file.read()

    audio_file_charles = open("Charles.midi", 'rb')
    st.session_state["audio_bytes_charles"] = audio_file_charles.read()

    audio_file_kick = open("Kick.midi", 'rb')
    st.session_state["audio_bytes_kick"] = audio_file_kick.read()

    audio_file_snare = open("Snare.midi", 'rb')
    st.session_state["audio_bytes_snare"] = audio_file_snare.read()

    st.balloons()

    st.session_state["Download"] = False
    st.session_state["Download_press"] = False

    st.session_state["Download_charles"] = False
    st.session_state["Download_press_charles"] = False

    st.session_state["Download_kick"] = False
    st.session_state["Download_press_kick"] = False

    st.session_state["Download_snare"] = False
    st.session_state["Download_press_snare"] = False

######################################################################
#Make the 4 download buttons, one for each sound

col1,col2,col3,col4=st.columns(4)
with col1:
    if st.session_state["Download"] == False:
        if st.download_button("Download Bass MIDI File", data=st.session_state["audio_bytes"], file_name=st.session_state["file_name"]):
            st.session_state["Download_press"] = True
with col2:
    if st.session_state["Download_charles"] == False:
        if st.download_button("Download Charles MIDI File", data=st.session_state["audio_bytes_charles"], file_name="Charles.midi"):
            st.session_state["Download_press_charles"] = True
with col3:
    if st.session_state["Download_kick"] == False:
        if st.download_button("Download Kick MIDI File", data=st.session_state["audio_bytes_kick"], file_name="Kick.midi"):
            st.session_state["Download_press_kick"] = True
with col4:
    if st.session_state["Download_snare"] == False:
        if st.download_button("Download Snare MIDI File", data=st.session_state["audio_bytes_snare"], file_name="Snare.midi"):
            st.session_state["Download_press_snare"] = True

######################################################################
#this last part of the code, makes the button download persist even through the re runs of the code.
#after it is press, it will disappear
if st.session_state['Download_press'] == True:
    st.session_state['Download'] = True
    url_gif_end="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExYzAyOGYwN2IxOTAwOTA3MTMwOTdlYTUyOGEyY2I4YzNmNDA2MWM1NSZlcD12MV9pbnRlcm5hbF9naWZzX2dpZklkJmN0PWc/M6IvtGig7gC4/giphy.gif"

    col1,col2=st.columns(2)
    with col1:
        st.image(url_gif_end, width=300)
    with col2:
        st.image(url_gif_end, width=300)

if st.session_state['Download_press_charles'] == True:
    st.session_state['Download_charles'] = True

if st.session_state['Download_press_kick'] == True:
    st.session_state['Download_kick'] = True

if st.session_state['Download_press_snare'] == True:
    st.session_state['Download_snare'] = True
