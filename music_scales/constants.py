"""Constant values for package"""

from enum import Enum

from .note import Note


NOTES = [
    Note('c'),
    Note('c♯/d♭'),
    Note('d'),
    Note('d♯/e♭'),
    Note('e'),
    Note('f'),
    Note('f♯/g♭'),
    Note('g'),
    Note('g♯/a♭'),
    Note('a'),
    Note('a♯/b♭'),
    Note('b')
]


class Tuning:
    """Guitar tunings"""
    STANDARD = ('e', 'a', 'd', 'g', 'b', 'e')


class Degree(Enum):
    """Degrees of a scale"""
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
    MINOR_NINTH = 'minor ninth'
    MAJOR_NINTH = 'major ninth'
    MINOR_TENTH = 'minor tenth'
    MAJOR_TENTH = 'major tenth'
    PERFECT_ELEVENTH = 'perfect eleventh'
    DIMINISHED_TWELFTH = 'diminished twelfth'
    PERFECT_TWELFTH = 'perfect twelfth'
    MINOR_THIRTEENTH = 'minor thirteenth'
    MAJOR_THIRTEENTH = 'major thirteenth'
    MINOR_FOURTEENTH = 'minor fourteenth'
    MAJOR_FOURTEENTH = 'major fourteenth'
    PERFECT_FIFTEENTH = 'perfect fifteenth'
    AUGMENTED_FIFTEENTH = 'augmented fifteenth'


DEGREES = (
    Degree.UNISON, Degree.MINOR_SECOND, Degree.MAJOR_SECOND,
    Degree.MINOR_THIRD, Degree.MAJOR_THIRD, Degree.PERFECT_FOURTH,
    Degree.DIMINISHED_FIFTH, Degree.PERFECT_FIFTH, Degree.MINOR_SIXTH,
    Degree.MAJOR_SIXTH, Degree.MINOR_SEVENTH, Degree.MAJOR_SEVENTH, Degree.OCTAVE
)
