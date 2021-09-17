"""Runs example code for music_scales package"""

from .concrete_scale import ConcreteScale
from .fretboard import Fretboard
from .note import Note
from . import SCALES


def run():
    """Runs example code for package"""
    fret_board = Fretboard()
    print(SCALES[0].name)
    frets_for_scale = fret_board.find_scale(SCALES[0].in_key('c'))
    assert frets_for_scale == [
        (0, 8, Note('c')),
        (0, 11, Note('d♯')),
        (1, 8, Note('f')),
        (1, 9, Note('f#')),
        (1, 10, Note('g')),
        (2, 8, Note('a#')),
        (2, 10, Note('c'))
    ]
    print(frets_for_scale)
    print(fret_board.find_scale(SCALES[0].in_key('c'), starting_string=3))
    concrete_scale = ConcreteScale(
        SCALES[0].in_key('c')
    )
    concrete_scale.as_image()


if __name__ == '__main__':
    run()
