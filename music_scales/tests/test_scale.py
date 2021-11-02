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
        (Note('c'), 'unison'),
        (Note('d'), 'major second'),
        (Note('e'), 'major third'),
        (Note('f'), 'perfect fourth'),
        (Note('f#'), 'diminished fifth'),
        (Note('a'), 'major sixth'),
    ]

    assert scale.with_degrees(Note('d#')) == [
        (Note('d#'), 'unison'),
        (Note('f'), 'major second'),
        (Note('g'), 'major third'),
        (Note('g#'), 'perfect fourth'),
        (Note('a'), 'diminished fifth'),
        (Note('c'), 'major sixth'),
    ]


def test_scale_repr():
    scale = Scale('foo_name', 'w w w+h', 'bar_mode')
    assert repr(scale) == "Scale('foo_name', 'w w w+h', 'bar_mode')"
