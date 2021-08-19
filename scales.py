NOTES = 'c c♯/d♭ d d♯/e♭ e f f#/g♭ g g#/a♭ a a#/b♭ b'
INTERVAL_NAMES = (
    'unison', 'minor second', 'major second', 'minor third',
    'major third', 'perfect fourth', 'diminished fifth',
    'perfect fifth', 'minor sixth', 'major sixth', 'minor seventh',
    'major seventh', 'octave'
)



class Note:
    def __init__(self, note):
        self.note = note

    def as_flat(self):
        pass

    def as_sharp(self):
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
        return [step[0] for step in self.with_intervals(key)]

    def with_intervals(self, key):
        notes = NOTES.split()

        if key not in notes:
            raise ValueError(f'"{key}" is not a valid key')

        notes_idx = notes.index(key)
        intervals_idx = 0

        key_notes = []

        for step in self._intervals:
            key_notes.append((notes[notes_idx], INTERVAL_NAMES[intervals_idx]))

            if step not in self.interval_to_steps:
                raise ValueError(f'Incorrect value "{step}" for scale interval')
            else:
                next_step = self.interval_to_steps[step]
                notes_idx += next_step
                intervals_idx += next_step

            notes_idx = notes_idx % len(notes)

        return key_notes


major = Scale('w w h w w w h')
print(major.in_key('c'))
print(major.with_intervals('c'))

minor = Scale('w h w w h w w')
print(minor.in_key('c'))

harmonic_minor = Scale('w h w w h w+h h')
print(harmonic_minor.in_key('c'))
