NOTES = 'c c# d d# e f f# g g# a a# b'


class Note:
    def __init__(self):
        pass


class Scale:

    interval_to_steps = {
        'h': 1,
        'w': 2,
        'w+h': 3
    }

    def __init__(self, intervals):
        self._intervals = intervals.split()

    def in_key(self, key):
        notes = NOTES.split()

        if key not in notes:
            raise ValueError(f'"{key}" is not a valid key')

        idx = notes.index(key)

        key_notes = []

        for step in self._intervals:
            key_notes.append(notes[idx])

            if step not in self.interval_to_steps:
                raise ValueError(f'Incorrect value "{step}" for scale interval')
            else:
                idx += self.interval_to_steps[step]

            idx = idx % len(notes)

        return key_notes


major = Scale('w w h w w w h')
print(major.in_key('c'))

minor = Scale('w h w w h w w')
print(minor.in_key('c'))

harmonic_minor = Scale('w h w w h w+h h')
print(harmonic_minor.in_key('c'))
