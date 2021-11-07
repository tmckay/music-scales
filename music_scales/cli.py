'''Command line interface to package'''
import argparse

from . import SCALES


def _get_args():
    parser = ArgumentParser()
    parser.add_argument('scale')
    parser.add_argument('key')
    return parser.parse_args()


def _find_scale(search_term):
    search_term = search_term.lower()

    for scale in SCALES:
        if scale.name.lower() == search_term:
            return scale


def main():
    args = _get_args()

    scale = _find_scale(args.scale)

    print(scale.in_key(Note(args.key)))
