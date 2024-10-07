from __future__ import annotations

from enum import Enum

def roman_to_integer(s: str) -> int:
    str_split = [a for a in s]
    
    nbr_split = [lookup_table(a) for a in str_split]

    j = 0
    value = 0
    while j < len(nbr_split):
        try:
            if nbr_split[j] >= nbr_split[j + 1]:
                value += nbr_split[j]
                j += 1
            elif nbr_split[j] < nbr_split[j + 1]:
                value += nbr_split[j+1] - nbr_split[j]
                j +=2
        except:
                value += nbr_split[j]
                j += 1

    return value

    # if descending == nbr_split:
    #     return sum(nbr_split)
    
    # if descending != nbr_split:
    #     length = len(nbr_split)

    #     first_part = sum(nbr_split[:length - 2])
    #     second_part = nbr_split[length - 1] - nbr_split[length - 2]

    #     return first_part + second_part


def lookup_table(s: str) -> int:
    if s == 'I':
        return 1
    
    if s == 'V':
        return 5
    
    if s == 'X':
        return 10
    if s == 'L':
        return 50
    if s == 'C':
        return 100
    if s == 'D':
        return 500
    if s == 'M':
        return 1000

if __name__ == "__main__":
    no = roman_to_integer("MCMXCIV")
    print(no)