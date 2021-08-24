from scale import Scale


SCALES = [
    Scale(name='blues', intervals='3h w h h 3h w'),
    Scale(name='harmonic minor', intervals='w h w w h 3h h'),
    Scale(name='major', intervals='w w h w w w h', mode='Ionian'),
    Scale(name='major pentatonic', intervals='w w 3h w 3h'),
    Scale(name='minor pentatonic', intervals='3h w w 3h w'),
    Scale(name='mixolydian', intervals='w w h w w h w'),
    Scale(name='natural minor', intervals='w h w w h w w', mode='Aeolian'),
]


if __name__ == '__main__':
    for scale in SCALES:
        print(scale.in_key('c'))
        print(scale.with_degrees('c'))
