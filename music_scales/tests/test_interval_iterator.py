from music_scales.constants import Degree
from music_scales.interval_iterator import IntervalIterator


def test_interval_iterator():
    interval_iterator = IntervalIterator(Degree.MINOR_THIRD)

    for idx, deg in enumerate(interval_iterator):
        if idx == 0:
            assert deg is Degree.MINOR_THIRD
        elif idx == 1:
            assert deg is Degree.MAJOR_THIRD
        else:
            break
