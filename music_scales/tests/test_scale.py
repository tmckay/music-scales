from music_scales.note import Note
from music_scales.scale import Scale


def test_scale_repr():
    scale = Scale('foo_name', 'w w', 'bar_mode')
    assert repr(scale) == "Scale('foo_name', 'w w', 'bar_mode')"


def test_scale_in_key():
    scale = Scale('foo', 'w w w h 3h')
    assert scale.in_key('c') == [
        Note('c'),
        Note('d'),
        Note('e'),
        Note('f#'),
        Note('g')
    ]
