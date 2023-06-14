import music21 as m21

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

    stream.write(format, fp=file_name)
    return stream
