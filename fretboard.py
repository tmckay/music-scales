from collections import deque
import math

from __init__ import SCALES
from constants import NOTES


class Fretboard:

    def __init__(self, tuning=['e', 'a', 'd', 'g', 'b', 'e'], number_frets=24):
        self.tuning = tuning
        self.number_frets = number_frets

    def find_scale(self, scale, starting_string=0, fret_reach_limit=3):
        """starting_string is index of string in tuning"""
        def find_fret_for_note(open_note, target_note):
            #print(f'looking for {target_note} on open string {open_note}')
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

        def are_frets_in_limit(fret_a, fret_b, limit):
            return math.abs(fret_b - fret_a) <= limit

        frets = []
        queue = deque()
        for note in scale:
            note = note.split('/')[0]
            #print(f'note in scale {note}')
            queue.append((starting_string, note))
            while len(queue) > 0:
                target = queue.popleft()
                result = find_fret_for_note(self.tuning[target[0]], target[1])

                if len(frets) > 0 and \
                    (abs(result - frets[-1][1]) > fret_reach_limit or\
                    abs(target[0] - frets[-1][0]) > 1):
                        queue.append((target[0] + 1, target[1]))
                else:
                    frets.append((target[0], result, target[1]))

        return frets


if __name__ == '__main__':
    fb = Fretboard()
    print(SCALES[0].name)
    frets_for_scale = fb.find_scale(SCALES[0].in_key('c'))
    assert frets_for_scale == [(0, 8, 'c'), (0, 11, 'd♯'), (1, 8, 'f'), (1, 9, 'f#'), (1, 10, 'g'), (2, 8, 'a#'), (2, 10, 'c')]
    print(frets_for_scale)
    print(fb.find_scale(SCALES[0].in_key('c'), starting_string=2))
