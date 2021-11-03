from music_scales.constants import Degree
from music_scales.note import Note
from music_scales.scale import Scale


def test_scale_in_key():
    scale = Scale('foo', 'w w w h w+h')
    assert scale.in_key('c') == [
        Note('c'),
        Note('d'),
        Note('e'),
        Note('f#'),
        Note('g'),
        Note('a#')
    ]


def test_scale_with_degrees():
    scale = Scale('foo', 'w w h h 3h')
    assert scale.with_degrees(Note('c')) == [
        (Note('c'), Degree.UNISON),
        (Note('d'), Degree.MAJOR_SECOND),
        (Note('e'), Degree.MAJOR_THIRD),
        (Note('f'), Degree.PERFECT_FOURTH),
        (Note('f#'), Degree.DIMINISHED_FIFTH),
        (Note('a'), Degree.MAJOR_SIXTH),
    ]

    assert scale.with_degrees(Note('d#')) == [
        (Note('d#'), Degree.UNISON),
        (Note('f'), Degree.MAJOR_SECOND),
        (Note('g'), Degree.MAJOR_THIRD),
        (Note('g#'), Degree.PERFECT_FOURTH),
        (Note('a'), Degree.DIMINISHED_FIFTH),
        (Note('c'), Degree.MAJOR_SIXTH),
    ]


def test_scale_repr():
    scale = Scale('foo_name', 'w w w+h', 'bar_mode')
    assert repr(scale) == "Scale('foo_name', 'w w w+h', 'bar_mode')"
