from __future__ import annotations
from typing import List


class Solution:
    def letterCombinations(digits: str) -> List[str]:
        number_letter_dict = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        digit_values = [i for i in digits]
        i = 0
        j = i + 1

        if len(digit_values) == 0:
            return []

        final_answer = []
        for m in number_letter_dict[digit_values[i]]:
            if j < len(digit_values):
                for n in number_letter_dict[digit_values[j]]:
                    final_answer.append(m + n)
                    # j += 1
                    # if j >= len(digit_values):
                    #     continue
            else:
                final_answer.append(m)
            # i += 1
            # if i > len(digit_values):
            #     continue
        return final_answer


print(Solution.letterCombinations(""))
