"""Misc utility functions"""

def to_ordinal(number: int):
    """Convert a number to an ordinal version of it"""
    ordinals = {
        11: '11th',
        12: '12th',
        13: '13th',
    }
    if number in ordinals:
        return ordinals[number]
    number_as_str = str(number)
    if number_as_str[-1] in ('1',):
        return f'{number_as_str}st'
    if number_as_str[-1] in ('2',):
        return f'{number_as_str}nd'
    if number_as_str[-1] in ('3',):
        return f'{number_as_str}rd'
    return f'{number_as_str}th'
