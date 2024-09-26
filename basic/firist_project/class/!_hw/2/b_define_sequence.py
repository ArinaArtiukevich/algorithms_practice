from enum import Enum


class Names(str, Enum):
    CONSTANT = 'CONSTANT'
    ASCENDING = 'ASCENDING'
    WEAKLY_ASCENDING = 'WEAKLY ASCENDING'
    DESCENDING = 'DESCENDING'
    WEAKLY_DESCENDING = 'WEAKLY DESCENDING'
    RANDOM = 'RANDOM'


if __name__ == '__main__':
    prev_element = int(input())
    if prev_element == -2000000000:
        print(Names.RANDOM.name)
    else:
        element = int(input())
        sequence_types = set()
        while element != -2000000000:
            if prev_element > element:
                sequence_types.add(Names.DESCENDING)
            elif prev_element < element:
                sequence_types.add(Names.ASCENDING)
            elif prev_element == element:
                sequence_types.add(Names.CONSTANT)
            prev_element = element
            element = int(input())

        if len(sequence_types) == 3:
            print(Names.RANDOM.name)
        elif len(sequence_types) == 1:
            print(sequence_types.pop().name)
        elif Names.CONSTANT in sequence_types:
            print(Names.WEAKLY_ASCENDING.name) if Names.ASCENDING in sequence_types else print(Names.WEAKLY_DESCENDING.name)
        else:
            print(Names.RANDOM.name)
