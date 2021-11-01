from music_scales.concrete_scale import ConcreteScale
from music_scales.note import Note


def test_concrete_scale():
    """Fails if we can't instantiate a ConcreteScale"""
    concrete_scale = ConcreteScale(
        'blues',
        Note('c'),
        [
            (0, 8, Note('c')),
            (0, 11, Note('d♯')),
            (1, 8, Note('f')),
            (1, 9, Note('f#')),
            (1, 10, Note('g')),
            (2, 8, Note('a#')),
            (2, 10, Note('c'))
        ]
    )
