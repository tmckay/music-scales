"""Concrete scale on a fretboard"""
from typing import List, Tuple

from .note import Note


class ConcreteScale:
    """A representation of a scale on a fretboard with
    actual string and frets"""

    def __init__(self, scale_def: List[Tuple[int, int, Note]]):
        """
        Args:
            scale_def: definition of a scale with format
                       List[Tuple[<guitar-string>, <fret>, Note]]
        """
        self.scale_def = scale_def

    def as_image(self):
        """Return image of scale on a fretboard"""
