
from user_input_processing import translate_input
from save_melody2 import save_melody2



def generate_drum_midi(charles_str,kick_str,snare_str):

    melodies = ["Charles.midi","Kick.midi","Snare.midi"]
    position = 0

    CH_list = charles_str.split(",")
    CH_list = [value == "True" for value in CH_list]

    CK_list = kick_str.split(",")
    CK_list = [value == "True" for value in CK_list]

    SN_list = snare_str.split(",")
    SN_list = [value == "True" for value in SN_list]

    X = [CH_list,CK_list,SN_list]
    print(X)
    X_mod = translate_input(X)
    for melody in X_mod:
        print(melodies[position])
        print(melody)
        save_melody2(melody, step_duration=0.25,format='midi', file_name= melodies[position])
        position += 1
