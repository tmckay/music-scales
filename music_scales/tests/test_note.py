from music_scales.note import Note


def test_note_equality():
    """Fails if notes don't equal when they should"""
    assert Note('c♯') == Note('c♯/d♭')
    assert Note('c') == 'c'
    assert not Note('c') == Note('c♯/d♭')
