'''Command line interface to package'''
import argparse

from .note import Note
from . import SCALES


def _get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('scale')
    parser.add_argument('key')
    return parser.parse_args()


def _find_scale(search_term):
    search_term = search_term.lower()
    found_scale = None

    for scale in SCALES:
        if scale.name.lower() == search_term:
            found_scale = scale
            break
    return found_scale


def main():
    '''Main entry point for CLI'''
    args = _get_args()

    scale = _find_scale(args.scale)

    print(scale.in_key(Note(args.key)))
