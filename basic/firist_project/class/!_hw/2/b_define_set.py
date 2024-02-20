# 5 4 4 6
from enum import Enum


class Names(str, Enum):
    CONSTANT = 'CONSTANT'
    ASCENDING = 'ASCENDING'
    WEAKLY_ASCENDING = 'WEAKLY ASCENDING'
    DESCENDING = 'DESCENDING'
    WEAKLY_DESCENDING = 'WEAKLY DESCENDING'
    RANDOM = 'RANDOM'
    DEFAULT = 'DEFAULT'


if __name__ == '__main__':
    prev_element = int(input())
    if prev_element == -2000000000:
        print(Names.CONSTANT.name)
    else:
        element = int(input())
        prev_name = Names.DEFAULT
        while element != -2000000000:
            if prev_element > element and prev_name == Names.DEFAULT:
                prev_name = Names.DESCENDING
            elif prev_element < element and prev_name == Names.DEFAULT:
                prev_name = Names.ASCENDING
            elif prev_element == element and prev_name == Names.DEFAULT:
                prev_name = Names.CONSTANT

            elif prev_element > element and prev_name == Names.CONSTANT:
                prev_name = Names.WEAKLY_DESCENDING
            elif prev_element < element and prev_name == Names.CONSTANT:
                prev_name = Names.WEAKLY_ASCENDING

            elif prev_element == element and prev_name == Names.ASCENDING:
                prev_name = Names.WEAKLY_ASCENDING
            elif prev_element == element and prev_name == Names.DESCENDING:
                prev_name = Names.WEAKLY_DESCENDING

            elif (prev_element > element and not (prev_name == Names.DESCENDING or prev_name == Names.DEFAULT or prev_name == Names.WEAKLY_DESCENDING)) or \
                    (prev_element < element and not (prev_name == Names.ASCENDING or prev_name == Names.DEFAULT or Names.WEAKLY_ASCENDING)):
                prev_name = Names.RANDOM
            prev_element = element
            element = int(input())
        print(prev_name.name if prev_name.name != Names.DEFAULT.name else Names.CONSTANT.name)
