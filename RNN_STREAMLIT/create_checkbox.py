import streamlit as st

@st.cache
def create_checkbox(text,key):
    #List of sounds, block of boxes for the two groups of 16th notes.

    # List of sounds for block
    sounds = {
        'Kick': [],
        'Snare': [],
        'Hi-Hat': []
    }

    contador = ["1", "e", "Y", "a", "2", "e", "Y", "a", "3", "e", "Y", "a", "4", "e", "Y", "a"]

    # First block of boxes
    st.write(text)
    for sound_name, sound_list in sounds.items():
        st.write(sound_name)
        cols = st.columns(16)

        for i, col in enumerate(cols):

            checkbox = col.checkbox(f' {contador[i]}', key="".join([str(i)+key, sound_name]))
            sound_list.append(checkbox)

    return sounds
