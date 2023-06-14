import streamlit as st

import streamlit as st

def create_checkbox(text, key):
    # List of sounds, block of boxes for the two groups of 16th notes.

    # List of sounds for block
    sounds = {
        'Kick': [],
        'Snare': [],
        'Hi-Hat': []
    }

    contador = ["1", "e", "&", "a", "2", "e", "&", "a", "3", "e", "&", "a", "4", "e", "&", "a"]

    # First block of boxes
    st.write(text)
    for sound_name, sound_list in sounds.items():
        st.write(sound_name)
        cols = st.columns(16)

        for i, col in enumerate(cols):
            if contador[i].isdigit():
                col.markdown(f"<p style='color:#FF6666'>{contador[i]}</p>", unsafe_allow_html=True)
            else:
                col.write(contador[i])
            checkbox = col.checkbox(f' {contador[i]}', key="".join([str(i) + key, sound_name]))
            sound_list.append(checkbox)

    return sounds
