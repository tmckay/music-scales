from typing import List, Tuple

from constants import NOTES, DEGREES, Degrees


class Scale:

    interval_to_steps = {
        'h': 1,
        'w': 2,
        'w+h': 3,
        '3h': 3,
    }

    def __init__(self, name: str, intervals: str, mode: str = None):
        self.name = name
        self.intervals = intervals.split()
        self.mode = mode 

    def in_key(self, key: str) -> List[str]:
        return [step[0] for step in self.with_degrees(key)]

    def with_degrees(self, key: str) -> List[Tuple[str, str]]:
        notes = NOTES.split()

        if key not in notes:
            raise ValueError(f'"{key}" is not a valid key')

        notes_idx = notes.index(key)
        intervals_idx = 0

        key_notes = []

        for step in self.intervals:
            key_notes.append((notes[notes_idx], DEGREES[intervals_idx]))

            if step not in self.interval_to_steps:
                raise ValueError(f'Incorrect value "{step}" for scale interval')
            else:
                next_step = self.interval_to_steps[step]
                notes_idx += next_step
                intervals_idx += next_step

            notes_idx = notes_idx % len(notes)

        return key_notes
