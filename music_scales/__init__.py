"""Provides music theory objects"""

from .note import Note
from .scale import Scale


SCALES = [
    Scale(name='blues', intervals='3h w h h 3h w w'),
    Scale(name='harmonic minor', intervals='w h w w h 3h h h'),
    Scale(name='major pentatonic', intervals='w w 3h w 3h 3h'),
    Scale(name='minor pentatonic', intervals='3h w w 3h w w'),
    Scale(name='major', intervals='w w h w w w h h', mode='Ionian'),
    Scale(name='Dorian', intervals='w h w w w h w w', mode='Dorian'),
    Scale(name='Phrygian', intervals='h w w w h w w w', mode='Phrygian'),
    Scale(name='Lydian', intervals='w w w h w w h h', mode='Lydian'),
    Scale(name='Mixolydian', intervals='w w h w w h w w', mode='Mixolydian'),
    Scale(name='natural minor', intervals='w h w w h w w w', mode='Aeolian'),
    Scale(name='Locrian', intervals='h w w h w w w w', mode='Locrian'),
]


if __name__ == '__main__':
    for scale in SCALES:
        print(scale.in_key(Note('c')))
        print(scale.with_degrees(Note('c')))
