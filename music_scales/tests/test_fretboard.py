from music_scales.fretboard import Fretboard
from music_scales.note import Note


def test_find_fret_for_note():
    fretboard = Fretboard()

    assert fretboard.find_fret_for_note(Note('e'), Note('a')) == 5

