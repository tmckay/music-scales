from __init__ import SCALES
from constants import NOTES


class Fretboard:

    def __init__(self, tuning=['e', 'a', 'd', 'g', 'b', 'e'], number_frets=24):
        self.tuning = tuning
        self.number_frets = number_frets

    def find_scale(self, scale, fret_reach_limit=3):
        def find_fret_for_note(open_note, target_note):
            print(f'looking for {target_note} on open string {open_note}')
            notes = NOTES.split()
            open_note_idx = -1 
            for idx, note in enumerate(notes):
                sub_notes = note.split('/')

                if open_note in sub_notes:
                    open_note_idx = idx

            fret = None
            fret_idx = 0
            note_idx = open_note_idx
            while fret is None:
                if target_note in notes[note_idx].split('/'):
                    fret = fret_idx
                else:
                    note_idx += 1
                    fret_idx += 1

                note_idx = note_idx % len(notes)
            return fret

        return find_fret_for_note('e', scale.in_key('c')[1].split('/')[0])


if __name__ == '__main__':
    fb = Fretboard()
    print(fb.find_scale(SCALES[0]))
