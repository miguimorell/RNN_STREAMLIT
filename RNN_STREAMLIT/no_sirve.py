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
