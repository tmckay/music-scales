from music_scales.scale import Scale


def test_scale():
    scale = Scale('foo_name', 'w w', 'bar_mode')
    assert repr(scale) == "Scale('foo_name', 'w w', 'bar_mode')"
