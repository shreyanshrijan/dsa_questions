from __future__ import annotations

import pandas as pd

def longest_common_prefix(strs: list[str]) -> str:

    length_of_word = [len(a) for a in strs]
    smallest_word_length = min(length_of_word)

    final_answer = []
    i = 0
    while i < smallest_word_length:
        letter = []
        for word in strs:
            letter.append(word[i])
        result = _check_letter(letter)

        if not result:
            return "".join(final_answer)
        
        final_answer.append(letter[0])
        i += 1

    return "".join(final_answer)
    
def _check_letter(lst: list) -> bool:
    if all(s == lst[0] for s in lst):
        return True
    else:
        return False
        
if __name__ == "__main__":
    a = longest_common_prefix([""])
    print(a)
