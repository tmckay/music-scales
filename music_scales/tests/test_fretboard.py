from music_scales.fretboard import Fretboard
from music_scales.note import Note
from music_scales import SCALES


def test_find_fret_for_note():
    fretboard = Fretboard()

    assert fretboard.find_fret_for_note(Note('e'), Note('a')) == 5


def test_find_fret_for_note_with_start_from():
    fretboard = Fretboard()

    assert fretboard.find_fret_for_note(
        Note('e'),
        Note('e'),
        start_from_fret=9
    ) == 12

    assert fretboard.find_fret_for_note(
        Note('e'),
        Note('e'),
    ) == 0

    assert fretboard.find_fret_for_note(
        Note('e'),
        Note('a'),
    ) == 5

    assert fretboard.find_fret_for_note(
        Note('e'),
        Note('f'),
        start_from_fret=12
    ) == 13


def test_build_note_cache():
    fretboard = Fretboard()
    fretboard._build_note_cache()
    assert sum([len(val) for val in fretboard._note_cache.values()]) == 6 * 25

    assert len(fretboard._note_cache['c']) == 12
    assert len(fretboard._note_cache['d♯/e♭']) == 12
    assert (1, 3) in fretboard._note_cache['c']


def test_find_scale():
    fretboard = Fretboard()

    assert fretboard.find_scale(
        scale=SCALES[0].in_key('c'),
        starting_string=0,
        fret_reach_limit=3
    ) == [
        (0, 8, Note('c')),
        (0, 11, Note('d♯/e♭')),
        (1, 8, Note('f')),
        (1, 9, Note('f#/g♭')),
        (1, 10, Note('g')),
        (2, 8, Note('a#/b♭')),
        (2, 10, Note('c'))
    ]
