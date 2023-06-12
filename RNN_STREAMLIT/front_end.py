import os
os.environ['SDL_AUDIODRIVER'] = 'directsound'

import streamlit as st
from PIL import Image
import numpy as np
import sounddevice as sd
import requests
import music21 as m21


import time

from playsound import playsound

url="http://127.0.0.1:8000/predict"

def save_melody(melody, step_duration=0.25,format='midi', file_name= 'test.mid'):
         #create a music 21 stream
         stream= m21.stream.Stream()

         #parse all the symbols in the melody and create note/rest objects
         #e.g. 60_ _ _ r_ 62_
         start_symbol= None
         step_counter= 1

         for i, symbol in  enumerate(melody):
             #handle case in which we have a note/rest.
             if symbol != "_":
                 pass
                 #ensure we're dealing with note/rest beyond the first one
                 if start_symbol is not None:
                     quarter_length_duration= step_duration * step_counter #0.25*4 = 1
                     #handle rest
                     if start_symbol== 'r':
                         m21_event= m21.note.Rest(quarterLenth= quarter_length_duration)
                     #handle note
                     else:
                         m21_event= m21.note.Note(int(start_symbol),quarterLenth=quarter_length_duration)

                     stream.append(m21_event)

                 #reset the step_counter
                     step_counter= 1

                 start_symbol = symbol

             #handle case in which we have a prolongation sign "_"
             else:
                 step_counter+= 1

         #write the m21 stream to a midifile
         stream.write(format, file_name)

         return stream

'''
# Grove-Nator 3000
'''

'''
## Tired of your friend not being able to play with you?....
## Do not worry, Grove-Nator3000 arrives to make your life easier...
'''

#List of sounds, block of boxes for the two groups of 16th notes.

# List of sounds for block 1
sounds2 = {
    'Kick': [],
    'Snare': [],
    'Hi-Hat': []
}

contador = ["1", "e", "Y", "a", "2", "e", "Y", "a", "3", "e", "Y", "a", "4", "e", "Y", "a"]

# First block of boxes
st.write("Enter the drums for the first bar:")
for sound_name, sound_list in sounds2.items():
    st.write(sound_name)
    cols = st.columns(16)

    for i, col in enumerate(cols):

        checkbox = col.checkbox(f' {contador[i]}', key="".join([str(i), sound_name]))
        sound_list.append(checkbox)

# Separator and text
st.write("---")
st.write("Enter the drums for the second bar:")

#Sounds for block 2
sounds2_second_block = {
    'Kick': [],
    'Snare': [],
    'Hihat': []
}

# Second block of boxes
for sound_name, sound_list in sounds2_second_block.items():
    st.write(sound_name)
    cols = st.columns(16)
    for i, col in enumerate(cols):
        checkbox = col.checkbox(f'{contador[i]}', key="".join([str(i + 100), sound_name]))
        sound_list.append(checkbox)
        #print(type(sound_list))


resultados_seleccionados1 = []
resultados_seleccionados2 = []


# Botón Submit
if st.button("Submit"):
    # Almacenar los resultados seleccionados en una lista
    selected1 = []
    selected2 = []

    # Primer bloque de cajas
    for sound_name, sound_list in sounds2.items():
        selected1.append(sound_list)
        if len(selected1)==3:

            kick_data=selected1[0]
            snare_data=selected1[1]
            charles_data=selected1[2]


    print("-----------------------------------------------------------------------")

    # Segundo bloque de cajas
    for sound_name, sound_list in sounds2_second_block.items():
        selected2.append(sound_list)

        if len(selected2)==3:

            kick_data2=selected2[0]
            print(type(kick_data2))
            print(kick_data2)
            snare_data2=selected2[1]
            charles_data2=selected2[2]



    print("kick data1")
    print(type(kick_data))
    print("kick data2")
    print(type(kick_data2))

    #Concatenar los outputs en 3 strings.
    #orden-> Charles, kick, snare
    #Sumar las listas de los dos bloques

    kick=kick_data+kick_data2
    snare=snare_data+snare_data2
    charles=charles_data+charles_data2

    kick_str = ",".join(str(elemento) for elemento in kick)

    snare_str = ",".join(str(elemento) for elemento in snare)

    charles_str = ",".join(str(elemento) for elemento in charles)


    #orden-> Charles, kick, snare
    #api:
    params={"CH":charles_str,"CK":charles_str,"SN":snare_str}

    query=requests.get(url,params).json()

    bass=[]
    for key, value in query.items():
        bass.append(value)



print(bass)
stream=save_melody(bass, step_duration=0.25,format='midi', file_name= 'test.mid')









"""
# Mostrar los resultados seleccionados para el primer bloque
st.write('Resultados seleccionados para el primer bloque:')
for sound_name, sound_list in sounds2.items():
    st.write(f'{sound_name}: {sound_list}')

# Mostrar los resultados seleccionados para el segundo bloque
st.write('Resultados seleccionados para el segundo bloque:')
for sound_name, sound_list in sounds2_second_block.items():
    st.write(f'{sound_name}: {sound_list}')

"""

















"""
######################################

# Cargar los archivos de sonido
kick_sound, _ = sf.read('Kick.wav')
snare_sound, _ = sf.read('Snare.wav')
hihat_sound, _ = sf.read('Hihat.wav')

# Función para reproducir los sonidos seleccionados
def play_sounds(sounds):
    rhythm = np.zeros(8, dtype=bool)
    for sound_name, sound_list in sounds2.items():
        for i, checkbox in enumerate(sound_list):
            if checkbox:
                if sound_name == 'K':
                    rhythm[i] = True
                elif sound_name == 'S':
                    rhythm[i + 8] = True
                elif sound_name == 'HH':
                    rhythm[i] = True
                    rhythm[i + 8] = True

    if rhythm.any():
        if rhythm[:8].any():
            sf.play(kick_sound)
        if rhythm[8:].any():
            sf.play(snare_sound)
            sf.play(hihat_sound)

# Botón para reproducir los sonidos seleccionados
if st.button('Reproducir Sonidos'):
    play_sounds(sounds)
"""

#####################################
