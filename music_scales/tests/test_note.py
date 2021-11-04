from music_scales.note import Note


def test_note_equality():
    """Fails if notes don't equal when they should"""
    assert Note('c♯') == Note('c♯/d♭')
    assert Note('c') == 'c'
    assert not Note('c') == Note('c♯/d♭')
    assert 'c♯' == Note('c♯')
    assert Note('C') == Note('c')
    assert Note('F#') == Note('f#')
    assert Note('E FLAT') == Note('Eb')


def test_normalize_note_str():
    note = Note('c')
    assert note._normalize_note_str('d#') == 'd♯'
    assert note._normalize_note_str('eb') == 'e♭'
    assert note._normalize_note_str('f sharp') == 'f♯'
    assert note._normalize_note_str('g flat') == 'g♭'


def test_note_hashable():
    {Note('c'): 'c'}
