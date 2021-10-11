"""Concrete scale on a fretboard"""
from typing import List, Tuple

from .fretboard_drawer import FretboardDrawer
from .note import Note
from .utils import to_ordinal


class ConcreteScale:
    """A representation of a scale on a fretboard with
    actual string and frets"""

    def __init__(self, name: str, key: str, scale_def: List[Tuple[int, int, Note]]):
        """
        Args:
            name: name of the scale
            scale_def: definition of a scale with format
                       List[Tuple[<guitar-string>, <fret>, Note]]
        """
        self.name = name
        self.key = key
        self.scale_def = scale_def

    @property
    def path_safe_key(self):
        """Returns a key that is path safe for saving images"""
        return str(self.key).split('/')[0]

    def as_image(self, width=800, height=800):
        """Return image of scale on a fretboard"""

        fretboard_drawer = FretboardDrawer(width, height)

        # show dots on strings for scale
        first_fret = self.scale_def[0][1]
        for idx, note in enumerate(self.scale_def):
            # label fret
            if idx == 0:
                ordinal = to_ordinal(note[1])
                fretboard_drawer.add_label(f'{ordinal} fret')

            fretboard_drawer.add_note(
                note[0],
                note[1],
                first_fret,
                idx in (0, len(self.scale_def)-1)
            )
        fretboard_drawer.save(f'/images/{self.name}_{self.path_safe_key}.png')
