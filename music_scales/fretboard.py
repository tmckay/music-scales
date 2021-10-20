"""Guitar fretboard object"""

from collections import defaultdict, deque, namedtuple
from typing import Deque, Dict, List, Tuple

from .constants import NOTES, Tuning
from .exceptions import UnresolvableScale
from .note import Note


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


class Fretboard:
    """Represents a guitar fretboard on a standard 6-string guitar.
    You can pass different tunings, but the default is standard tuning."""

    def __init__(self,
                 tuning: Tuple = Tuning.STANDARD,
                 number_frets: int = 24
        ):
        self.tuning = tuning
        self.number_frets = number_frets
        self._note_cache: Dict = {}

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

    def _build_note_cache(self):
        """Builds cache of all notes on fretboard"""
        note_cache = defaultdict(list)

        for string, open_note in enumerate(self.tuning):

            # Find open note within notes sequence
            for idx, note in enumerate(NOTES):
                if open_note == note:
                    note_idx = idx

            fret = 0
            while fret <= self.number_frets:
                current_note = NOTES[note_idx]

                note_cache[current_note].append((string, fret))

                fret += 1
                note_idx += 1
                note_idx = note_idx % len(NOTES)

        self._note_cache = note_cache

    def find_scale_hashmap_version(self, scale: List[str], starting_string: int = 0,
                                   fret_reach_limit: int = 4) -> List:
        """Hashmap version of finding a scale that uses a precomputed note index"""
        scale_fingerings = []
        string = starting_string

        def _get_scale_fingering(candidates):
            nonlocal string
            while string < len(self.tuning):
                # only consider notes on the right string
                on_string = [candidate for candidate in candidates if candidate[0] == string]

                # special case first notes
                if idx == 0:
                    # choose lowest allowable fret position on
                    # the starting_string
                    lowest_fret = sorted(on_string, key=lambda x: x[1])[0]
                    return lowest_fret

                within_reach = [candidate for candidate in candidates
                                if abs(candidate[1] - scale_fingerings[-1][1]) <= fret_reach_limit]
                if len(within_reach) > 0:
                    # keep the first option that works
                    return within_reach[0]
                else:
                    # increment string and try again
                    string += 1

        for idx, note in enumerate(scale):
            candidates = self._note_cache[note]

            scale_fingerings.append(_get_scale_fingering(candidates))

        return scale_fingerings

    def find_scale(self, scale: List[str], starting_string: int = 0,
                   fret_reach_limit: int = 4) -> List:
        """
        Args:
            scale: scale to generate frets for
            starting_string: index of string in tuning
            fret_reach_limit: number of frets between two notes
        """
        frets: List[NoteFound] = []
        queue: Deque[NoteSearch] = deque()

        for idx, note in enumerate(scale):

            queue.append(NoteSearch(starting_string, note))

            while len(queue) > 0:
                target = queue.popleft()

                # we've iterated through all the strings and
                # haven't found a note that meets all criteria
                if target.string >= len(self.tuning):
                    raise UnresolvableScale(f'Could not find note {note} / {idx}')

                starting_fret = 0  # start searching from the open string
                if len(frets) > 0:  # check if this is the first note we're finding
                    starting_fret = frets[0].fret  # start searching from
                                                   # fret of first note of scale
                    starting_fret -= 3  # search two notes up from last fret
                    starting_fret = max(starting_fret, 0)  # unless it's 0 or an open string

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
                    queue.append(NoteSearch(target.string + 1, target.note))
                # If everything is good, add the fret
                else:
                    frets.append(NoteFound(target.string, result, target.note))
                    starting_string = target.string

        return frets
