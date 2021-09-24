def to_ordinal(number: int):
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
    elif number_as_str[-1] in ('2',):
        return f'{number_as_str}nd'
    elif number_as_str[-1] in ('3',):
        return f'{number_as_str}rd'
    else:
        return f'{number_as_str}th'
