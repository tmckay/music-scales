from collections import deque
import math
from typing import List, Tuple

from __init__ import SCALES
from constants import NOTES
from scale import Scale


class Fretboard:

    def __init__(self, tuning: List = ['e', 'a', 'd', 'g', 'b', 'e'], number_frets: int = 24):
        self.tuning = tuning
        self.number_frets = number_frets

    @staticmethod
    def find_fret_for_note(open_note: str, target_note: str) -> int:
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

    @staticmethod
    def are_frets_in_limit(fret_a: str, fret_b: str , limit: int) -> bool:
        return abs(fret_b - fret_a) <= limit

    def find_scale(self, scale: Scale, starting_string: int = 0, fret_reach_limit: int = 3) -> List[Tuple]:
        """starting_string is index of string in tuning"""
        frets = []
        queue = deque()
        for note in scale:
            note = note.split('/')[0]
            queue.append((starting_string, note))
            while len(queue) > 0:
                target = queue.popleft()
                result = self.find_fret_for_note(self.tuning[target[0]], target[1])

                if len(frets) > 0 and \
                    (not self.are_frets_in_limit(result, frets[-1][1], fret_reach_limit) or\
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
