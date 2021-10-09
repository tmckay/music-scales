"""Guitar fretboard object"""

from collections import deque, namedtuple
from typing import Deque, List, Tuple

from .constants import NOTES, Tuning
from .exceptions import UnresolvableScale
from .note import Note


class Fretboard:
    """Represents a guitar fretboard on a standard 6-string guitar.
    You can pass different tunings, but the default is standard tuning."""

    def __init__(self,
                 tuning: Tuple = Tuning.STANDARD,
                 number_frets: int = 24
        ):
        self.tuning = tuning
        self.number_frets = number_frets

    @staticmethod
    def find_fret_for_note(
        open_note: Note,
        target_note: Note,
        start_from_fret: int = 0) -> int:
        """Look for a note and return the fret number for it

        open_note: the note of the string on the guitar at fret 0 aka open
        target_note: the note to find on the string
        """

        # Find open note within notes sequence
        for idx, note in enumerate(NOTES):
            if open_note == note:
                note_idx = idx

        fret = 0
        while fret < start_from_fret:
            fret += 1
            note_idx += 1
            note_idx = note_idx % len(NOTES)

        # Find fret of note on string
        while True:
            if target_note == NOTES[note_idx]:
                break

            note_idx += 1
            fret += 1
            note_idx = note_idx % len(NOTES)

        return fret

    @staticmethod
    def are_frets_in_limit(fret_a: int, fret_b: int , limit: int) -> bool:
        """Return if two frets are within a certain distance"""
        return abs(fret_b - fret_a) <= limit

    def find_scale(self, scale: List[str], starting_string: int = 0,
                   fret_reach_limit: int = 4) -> List[Tuple]:
        """
        Args:
            scale: scale to generate frets for
            starting_string: index of string in tuning
            fret_reach_limit: number of frets between two notes
        """

        NoteSearch = namedtuple('NoteSearch', [
                'string',
                'note'
            ]
        )
        NoteFound = namedtuple('NoteFound', [
                'string',
                'fret',
                'note'
            ]
        )
        frets: List[Tuple[NoteFound]] = []
        queue: Deque[Tuple[NoteSearch]] = deque()

        for idx, note in enumerate(scale):

            queue.append(NoteSearch(starting_string, note))

            while len(queue) > 0:
                target = queue.popleft()

                if target.string >= len(self.tuning):
                    raise UnresolvableScale(f'Could not find note {note} / {idx}')

                starting_fret = 0
                if len(frets) > 0:
                    # start from last fret
                    starting_fret = frets[0].fret
                    # give a little extra space
                    starting_fret -= 2
                    # unless it's less than 0
                    starting_fret = max(starting_fret, 0)

                result = self.find_fret_for_note(
                    self.tuning[target.string],
                    target.note,
                    starting_fret
                )

                # Accept first note that matches
                if len(frets) == 0:
                    frets.append(NoteFound(target.string, result, target.note))
                # For non-first notes, check that frets are
                # not too far apart
                elif not self.are_frets_in_limit(
                    result,
                    frets[0].fret,
                    fret_reach_limit
                ):
                    queue.append(NoteSearch(target.string + 1, target.note))

                # Make sure the strings are adjacent
                elif abs(target.string - frets[-1].string) > 1:
                    queue.append(NoteSearch(target.string + 1, target.fret))
                # If everything is good, add the fret
                else:
                    frets.append(NoteFound(target.string, result, target.note))
                    starting_string = target.string

        return frets
