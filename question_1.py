from __future__ import annotations


def find_common_prefix(lst: list[str]):
    common_strings = []
    i = 0
    minimum_length_word = min(lst)
    answer_string = []

    while i < minimum_length_word:
        for word in lst:
            common_strings.append(word[i])

        result = _all_values_same(common_strings)
        i = i + 1
        if result:
            answer_string.append(common_strings[0])
        else:
            return "".join(answer_string)
            
    return "".join(answer_string)


def _all_values_same(lst):
    reference_letter = lst[0]
    flag = True
    for letter in lst:
        if reference_letter != letter:
            flag = False

    return flag
        