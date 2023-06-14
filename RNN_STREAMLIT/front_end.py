import streamlit as st
from save_melody2 import save_melody2
from create_checkbox import create_checkbox
from insert_temperature import insert_temperature
from check_checkbox import check_checkbox
from call_api import call_api






# Configurar el ancho de las columnas
column1, column2, column3 = st.beta_columns(3)

# Columna 1
with column1:
    # Mostrar un GIF desde una URL
    url_gif = 'https://media2.giphy.com/media/xRYN8w3CKPcv6/giphy.gif?cid=ecf05e47ataqoy877rlderctx8xbcb7mqzsgi8tm8r3ginfd&ep=v1_gifs_search&rid=giphy.gif&ct=g'

    # Mostrar el GIF con un tamaño reducido
    st.image(url_gif, use_column_width=True)


# Columna 2
with column2:
    url_logo ='https://st2.depositphotos.com/15317184/46760/v/600/depositphotos_467603324-stock-illustration-p-letter-logo-letter-p.jpg'


# Mostrar logo
    st.image(url_logo, width=600)

    # Texto más pequeño con estilo personalizado
    st.markdown("<p style='font-size: 18px;'>Need some inspiration for your music creation?</p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 18px;'>Need a companion to spice up your drum grooves?</p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 18px;'>Sick of your current bass player and want to look for a replacement?</p>", unsafe_allow_html=True)


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



# Columna 3
with column3:
    st.image('ruta_de_la_imagen_2', use_column_width=True)
    # Otros contenidos de la columna 3
