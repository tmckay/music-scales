NOTES = 'c c# d d# e f f# g g# a a# b'


class Note:
    def __init__(self):
        pass


class Scale:
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

            if step == 'w':
                idx += 2
            elif step == 'h':
                idx += 1
            else:
                raise ValueError(f'Incorrect value "{step}" for scale interval')

            idx = idx % len(notes)

        return key_notes


major = Scale('w w h w w w h')
print(major.in_key('c'))
