"""Runs example code for music_scales package"""

from .fretboard import Fretboard
from . import SCALES


def run():
    """Runs example code for package"""
    fret_board = Fretboard()
    print(SCALES[0].name)
    frets_for_scale = fret_board.find_scale(SCALES[0].in_key('c'))
    #assert frets_for_scale == [
    #    (0, 8, 'c'),
    #    (0, 11, 'd♯'),
    #    (1, 8, 'f'),
    #    (1, 9, 'f#'),
    #    (1, 10, 'g'),
    #    (2, 8, 'a#'),
    #    (2, 10, 'c')
    #]
    print(frets_for_scale)
    print(fret_board.find_scale(SCALES[0].in_key('c'), starting_string=2))


if __name__ == '__main__':
    run()
