from music_scales.fretboard import Fretboard
from music_scales.note import Note
from music_scales import SCALES


def test_find_fret_for_note():
    fretboard = Fretboard()

    assert fretboard.find_fret_for_note(Note('e'), Note('a')) == 5


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
