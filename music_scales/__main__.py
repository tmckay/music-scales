"""Runs example code for music_scales package"""

import argparse

from .concrete_scale import ConcreteScale
from .constants import NOTES
from .fretboard import Fretboard
from .note import Note
from . import SCALES


def get_args() -> argparse.Namespace:
    """Get arguments from command line"""
    parser = argparse.ArgumentParser()
    parser.add_argument('--demo', default=False, action='store_true')
    parser.add_argument('--web', default=False, action='store_true')
    return parser.parse_args()


def run_demo():
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
    for idx, _ in enumerate(SCALES):
        concrete_scale = ConcreteScale(
            SCALES[idx].name,
            Note('c'),
            fret_board.find_scale(SCALES[idx].in_key('c'))
        )
        concrete_scale.as_image()


def run_web():
    """Run code to generate web site"""
    fret_board = Fretboard()

    for scale in SCALES:
        for note in NOTES:
            print(f'Generating image for {scale.name} in key of {note}')
            concrete_scale = ConcreteScale(
                scale.name,
                note,
                fret_board.find_scale(scale.in_key(note))
            )
            concrete_scale.as_image()


def main():
    """Main entrypoint"""
    args = get_args()

    if args.demo:
        run_demo()
    if args.web:
        run_web()


if __name__ == '__main__':
    main()
