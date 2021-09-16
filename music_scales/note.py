"""Represents a single musical note"""

class Note:
    """A music note including enharmonic equivalent"""
    def __init__(self, note: str):
        self.note = note

    def __eq__(self, other):
        if hasattr(other, 'note'):
            if self.note == other.note:
                return True
            if other.note in self.note.split('/'):
                return True
            if self.note in other.note.split('/'):
                return True
        else:  # assume str
            if other in self.note.split('/'):
                return True
        return False

    def __str__(self):
        return self.note

    def __repr__(self):
        return f'Note(\'{self.note}\')'
