

def check_checkbox(sounds):

    selected = []

    for sound_name, sound_list in sounds.items():
        selected.append(sound_list)
        if len(selected)==3:

            kick_data=selected[0]
            snare_data=selected[1]
            charles_data=selected[2]

    return kick_data,snare_data,charles_data
