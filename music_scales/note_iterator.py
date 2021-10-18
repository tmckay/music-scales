"""Note iterator for simplifying iterating through notes"""
from .note import Note
from .constants import NOTES


class NoteIterator:
    """Iterators through notes indefinitely"""
    def __init__(self, start_at: Note):
        self.note_idx = -1

        # Find open note within notes sequence
        for idx, note in enumerate(NOTES):
            if note == start_at:
                self.note_idx = idx

    def __iter__(self):
        return self

    def __next__(self):
        next_note = NOTES[self.note_idx]
        self.note_idx += 1
        self.note_idx = self.note_idx % len(NOTES)
        return next_note
