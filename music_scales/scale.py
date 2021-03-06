"""Module for representing a musical scale"""

from typing import List, Tuple

from .constants import Degree, DEGREES
from .note import Note
from .note_iterator import NoteIterator


class Scale:
    """A musical scale"""

    interval_to_steps = {
        'h': 1,
        'w': 2,
        'w+h': 3,
        '3h': 3,
    }

    def __init__(self, name: str, intervals: str, mode: str = None):
        """
        Args:
            name: name of the scale e.g. minor pentatonic
            intervals: scale intervals as 'w h' etc
            mode: name of the mode associated with the scale
        """

        self.name = name
        self.intervals = intervals.split()
        self.mode = mode

    def in_key(self, key: Note) -> List[Note]:
        """Generates the notes for the scale in the specified key

        Args:
            key: the key of the scale to generate e.g. 'c' or 'd'
        """
        return [step[0] for step in self.with_degrees(key)]

    def with_degrees(self, key: Note) -> List[Tuple[Note, Degree]]:
        """Generate notes of scale and include degrees e.g. 'major third'

        Args:
            key: the key of the scale to generate e.g. 'c' or 'd'
        """
        note_iterator = NoteIterator(key)
        intervals_idx = 0

        key_notes = []
        # Add first note / key of scale
        key_notes.append(
            (next(note_iterator), DEGREES[intervals_idx])
        )

        for step in self.intervals:

            if step not in self.interval_to_steps:
                raise ValueError(f'Incorrect value "{step}" for scale interval')

            next_step = self.interval_to_steps[step]
            for _ in range(next_step):
                next_note = next(note_iterator)
            intervals_idx += next_step

            key_notes.append((next_note, DEGREES[intervals_idx]))

        return key_notes

    def __repr__(self):
        intervals = ' '.join(self.intervals)
        first_segment = f"Scale('{self.name}', '{intervals}'"
        if self.mode:
            first_segment = first_segment + f", '{self.mode}'"
        return first_segment + ')'
