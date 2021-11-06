from music_scales.note import Note
from music_scales.note_iterator import NoteIterator


def test_note_iterator():
    note_iterator = NoteIterator(Note('c'))

    for idx, note in enumerate(note_iterator):
        if idx == 0:
            assert note == Note('c')
        elif idx == 1:
            assert note == Note('c#')
        else:
            break

def test_note_iterator_next():
    note_iterator = NoteIterator(Note('d#'))

    assert next(note_iterator) == Note('d#')
