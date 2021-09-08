"""Guitar fretboard object"""

from collections import deque
from typing import Deque, List, Tuple

from . import SCALES, constants


class Fretboard:
    """Represents a guitar fretboard on a standard 6-string guitar.
    You can pass different tunings, but the default is standard tuning."""

    def __init__(self, tuning: Tuple = ('e', 'a', 'd', 'g', 'b', 'e'), number_frets: int = 24):
        self.tuning = tuning
        self.number_frets = number_frets

    @staticmethod
    def find_fret_for_note(open_note: str, target_note: str) -> int:
        """Look for a note and return the fret number for it"""
        notes = constants.NOTES.split()
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
    def are_frets_in_limit(fret_a: int, fret_b: int , limit: int) -> bool:
        """Return if two frets are within a certain distance"""
        return abs(fret_b - fret_a) <= limit

    def find_scale(
        self,
        scale: List[str],
        starting_string: int = 0,
        fret_reach_limit: int = 3) -> List[Tuple]:
        """starting_string is index of string in tuning"""
        frets: List[Tuple] = []
        queue: Deque[Tuple] = deque()
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
    assert frets_for_scale == [
        (0, 8, 'c'),
        (0, 11, 'd♯'),
        (1, 8, 'f'),
        (1, 9, 'f#'),
        (1, 10, 'g'),
        (2, 8, 'a#'),
        (2, 10, 'c')
    ]
    print(frets_for_scale)
    print(fb.find_scale(SCALES[0].in_key('c'), starting_string=2))
