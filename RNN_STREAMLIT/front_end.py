import os
os.environ['SDL_AUDIODRIVER'] = 'directsound'

import streamlit as st
#from PIL import Image
#import numpy as np
#import sounddevice as sd
import requests
import music21 as m21
from pydub import AudioSegment
#from midi2audio import FluidSynth
import fluidsynth

import time

from playsound import playsound


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


def save_melody2(melody, step_duration=0.25, format='midi', file_name='./test.mid'):
    stream = m21.stream.Stream()
    start_symbol = None
    step_counter = 1

    for i, symbol in enumerate(melody):
        if symbol != "_":
            if start_symbol is not None:
                quarter_length_duration = step_duration * step_counter
                if start_symbol == 'r':
                    m21_event = m21.note.Rest(quarterLength=quarter_length_duration)
                else:
                    m21_event = m21.note.Note(int(start_symbol), quarterLength=quarter_length_duration)

                stream.append(m21_event)

            step_counter = 1
            start_symbol = symbol

        else:
            step_counter += 1

    stream=stream.write(format, file_name)
    musica = open('test.mid',"rb")
    midi_file = 'test.mid'
    audio_bytes = musica.read()
    st.audio(audio_bytes)
    return midi_file


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

#Botton to specify temperature
st.write("¨Temperature¨ is a parameter that adds randomness to the generation: Numbers closer to 0 make the model more deterministic. Numbers closer to 1 makes the generation more unpredictable.")
temperature = st.slider('Select a value for the temperature', 0.0, 1.0, step=0.1)
if st.button('Save value'):
    st.session_state['temperature']=temperature
    st.write('Value saved correctly!')




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


    #orden-> Charles, kick, snare
    #api:


    #url="http://127.0.0.1:8000/predict"
    url="https://rnnmusicgenerator-pdjk6hbk2a-ew.a.run.app/predict"
    params={"CH":charles_str,"CK":charles_str,"SN":snare_str,"T":st.session_state["temperature"]}

    query=requests.get(url,params).json()

    bass=[]
    for key, value in query.items():
        bass.append(value)


    if st.button('Download MIDI'):

        # Save the melody as a MIDI file
        st.session_state["melody"]=save_melody2(bass, step_duration=0.25,format='midi', file_name= 'test.mid')
        st.write(st.session_state["melody"])
        musica = open('./test.mid',"rb")
        audio_bytes = musica.read()
        st.audio(audio_bytes)
        # Provide the file path and a custom name for the download
        st.download_button(
            label='Download',
            data='st.session_state["melody"]',  # Provide the file path
            file_name='custom_filename.mid',
            mimi='audio/midi'
        )

    """
    FluidSynth(
        sound_font='/Users/Cris/code/miguimorell/RNN_STREAMLIT/RNN_STREAMLIT/GeneralUser GS v1.471.sf2',
        sample_rate=48000,
        ).midi_to_audio('/Users/Cris/code/miguimorell/RNN_STREAMLIT/RNN_STREAMLIT/test.mid', 'bass3.wav')

    audio_file = open('bass3.wav', 'rb')
    audio_bytes = audio_file.read()

    st.audio(audio_bytes)
    """

"""
######################################
# Load the sound files
kick_sound = AudioSegment.from_wav('Kick.wav')
snare_sound = AudioSegment.from_wav('Snare.wav')
hihat_sound = AudioSegment.from_wav('Hihat.wav')

# Function to play the selected sounds
def play_sounds(sounds):
    combined_kick = []
    combined_snare = []
    combined_charles = []
    combined_sounds = []
    for sound_name, sound_list in sounds.items():
        for i, checkbox in enumerate(sound_list):
            if checkbox:
                if sound_name == 'Kick':
                    combined_kick.append(kick_sound)
                elif sound_name == 'Snare':
                    combined_snare.append(snare_sound)
                elif sound_name == 'Hi-Hat':
                    combined_charles.append(hihat_sound)
            elif checkbox == False:
                if sound_name == 'Kick':
                    combined_kick.append(0)
                elif sound_name == 'Snare':
                    combined_snare.append(0)
                elif sound_name == 'Hi-Hat':
                    combined_charles.append(0)

    output_file = 'drums.wav'
    for i in range(0,len(combined_charles)):
        if combined_kick[i] == 0 and combined_snare[i] == 0 and combined_charles[i] == 0:
            pass
        elif combined_kick[i] == 0 and combined_snare[i] == 0:
            combined_sounds.append(combined_charles[i])
        elif combined_charles[i] == 0 and combined_snare[i] == 0:
            combined_sounds.append(combined_kick[i])
        elif combined_kick[i] == 0 and combined_charles[i] == 0:
            combined_sounds.append(combined_snare[i])
        elif combined_kick[i] == 0:
            combined_sounds.append(combined_snare[i].overlay(combined_charles[i]))
        elif combined_snare[i] == 0:
            combined_sounds.append(combined_kick[i].overlay(combined_charles[i]))
        elif combined_charles[i] == 0:
            combined_sounds.append(combined_kick[i].overlay(combined_snare[i]))
        else:
            combined_sounds.append(combined_kick[i].overlay(combined_snare[i]).overlay(combined_charles[i]))

    combined_audio = sum(combined_sounds)

    # Speed up the audio segment
    #speed_factor = 1  # Increase the speed by 1.5 times
    #sped_up_audio = combined_audio.speedup(playback_speed=speed_factor)

    combined_audio.export(output_file, format='wav')

    audio_file = open('drums.wav', 'rb')
    audio_bytes = audio_file.read()

    st.audio(audio_bytes)


# Button to play the selected sounds
if st.button('Reproducir Sonidos'):
    sounds = {
        'Kick': st.session_state['kick'],
        'Snare': st.session_state['snare'],
        'Hi-Hat': st.session_state['charles']
    }
    play_sounds(sounds)
"""
