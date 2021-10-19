from music_scales.fretboard import Fretboard, NoteFound
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

    assert len(fretboard._note_cache[Note('c')]) == 12
    assert len(fretboard._note_cache[Note('d♯/e♭')]) == 12
    assert (1, 3) in fretboard._note_cache[Note('c')]
    assert (0, 8) in fretboard._note_cache[Note('c')]
    assert (4, 1) in fretboard._note_cache[Note('c')]
    assert (4, 13) in fretboard._note_cache[Note('c')]
    assert (1, 15) in fretboard._note_cache[Note('c')]
    assert (2, 10) in fretboard._note_cache[Note('c')]
    assert (2, 11) not in fretboard._note_cache[Note('c')]
    assert (0, 11) in fretboard._note_cache[Note('d♯/e♭')]


def test_find_scale_hashmap_version():
    fretboard = Fretboard()
    fretboard._build_note_cache()
    
    assert len(fretboard.find_scale(
        scale=SCALES[0].in_key('c'),
        starting_string=0,
        fret_reach_limit=4
    )) == 7 

    assert fretboard.find_scale(
        scale=SCALES[0].in_key('c'),
        starting_string=0,
        fret_reach_limit=4
    ) == [
        NoteFound(string=0, fret=8, note=Note('c')),
        NoteFound(string=0, fret=11, note=Note('d♯/e♭')),
        NoteFound(string=1, fret=8, note=Note('f')),
        NoteFound(string=1, fret=9, note=Note('f♯/g♭')),
        NoteFound(string=1, fret=10, note=Note('g')),
        NoteFound(string=2, fret=8, note=Note('a♯/b♭')),
        NoteFound(string=2, fret=10, note=Note('c'))
    ]


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
        (1, 9, Note('f♯/g♭')),
        (1, 10, Note('g')),
        (2, 8, Note('a♯/b♭')),
        (2, 10, Note('c'))
    ]
