"""Represents a single musical note"""
import re
from typing import Tuple


class Note:
    """A music note including enharmonic equivalent"""

    _chromatic_scale = [
        ('c',),
        ('c♯', 'd♭'),
        ('d',),
        ('d♯', 'e♭'),
        ('e',),
        ('f',),
        ('f♯', 'g♭'),
        ('g',),
        ('g♯', 'a♭'),
        ('a',),
        ('a♯', 'b♭'),
        ('b',),
    ]

    def __init__(self, note: str):
        if '/' in note:
            note = note.split('/')[0]

        self.note = self._normalize_enharmonic_equivalent(
            self._normalize_note_str(note)
        )

    @staticmethod
    def _normalize_note_str(note: str) -> str:
        replacements = [
            (r'([a-g]{1})#', r'\1♯'),
            (r'([a-g]{1})b', r'\1♭'),
            (r'([a-g]{1}) sharp', r'\1♯'),
            (r'([a-g]{1}) flat', r'\1♭'),
        ]
        for replacement in replacements:
            note = re.sub(*replacement, note)
        return note

    def _normalize_enharmonic_equivalent(self, note: str) -> Tuple[str, ...]:

        # ensure we have enharmonic equivalents
        for notes in self._chromatic_scale:
            if note in notes:
                return notes

        raise ValueError(f'Value for note {note} in invalid')

    def __eq__(self, other):
        if hasattr(other, 'note'):
            return self.note == other.note

        # assume str
        return other in self.note

    def __hash__(self):
        return hash(self.note)

    def __str__(self):
        return '/'.join(self.note)

    def __repr__(self):
        return f'Note(\'{self.note}\')'
