'''Provides an iterator that loops through intervals / degrees'''
from .constants import Degree, DEGREES


class IntervalIterator:
    '''Iterates through intervals indefinitely'''
    def __init__(self, start_at: Degree):
        self.deg_idx = -1

        # Find starting point
        for idx, degree in enumerate(DEGREES):
            if degree == start_at:
                self.deg_idx = idx

    def __iter__(self):
        return self

    def __next__(self):
        next_deg = DEGREES[self.deg_idx]
        self.deg_idx += 1
        self.deg_idx = self.deg_idx % len(DEGREES)
        return next_deg
