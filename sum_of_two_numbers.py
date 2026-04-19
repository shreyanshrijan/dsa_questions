from __future__ import annotations


def match_the_sum(lst: list, target: int):
    for ind, num in enumerate(lst):
        i = 1
        while ind + i < len(lst):
            sum = lst[ind] + lst[ind + i]
            if sum == target:
                return (lst[ind], lst[ind + i])
            i = i + 1


def match_the_sum(lst: list, target: int):
    lst = sorted(lst)
    i = 0
    j = -1
    while i < len(lst) & j < len(lst):
        first_value = lst[i]
        second_value = lst[j]

        if first_value + second_value < target:
            i = i + 1

        if first_value + second_value > target:
            j = j - 1


        if first_value + second_value == target:
            return (first_value, second_value)

[10, 5, 25] 45
[5, 10, 25]
def match_the_sum(lst: list, target: int):
    