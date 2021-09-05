from enum import Enum


NOTES = 'c c♯/d♭ d d♯/e♭ e f f#/g♭ g g#/a♭ a a#/b♭ b'
DEGREES = (
    'unison', 'minor second', 'major second', 'minor third',
    'major third', 'perfect fourth', 'diminished fifth',
    'perfect fifth', 'minor sixth', 'major sixth', 'minor seventh',
    'major seventh', 'octave'
)

class Degree(Enum):
    UNISON = 'unison'
    MINOR_SECOND = 'minor second'
    MAJOR_SECOND = 'major second'
    MINOR_THIRD = 'minor third'
    MAJOR_THIRD = 'major third'
    PERFECT_FOURTH = 'perfect fourth'
    DIMINISHED_FIFTH = 'diminished fifth'
    PERFECT_FIFTH = 'perfect fifth'
    MINOR_SIXTH = 'minor sixth'
    MAJOR_SIXTH = 'major sixth'
    MINOR_SEVENTH = 'minor seventh'
    MAJOR_SEVENTH = 'major seventh'
    OCTAVE = 'octave'
