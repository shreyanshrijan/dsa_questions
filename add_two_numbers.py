from __future__ import annotations


class AddTwoNumbers:
    def _add(l1: list[int], l2: list[int]) -> list[int]:
        l1.reverse()
        l2.reverse()
        n1 = int("".join([str(i) for i in l1]))
        n2 = int("".join([str(i) for i in l2]))

        n: int = str(n1 + n2)
        final_number = [int(i) for i in [charecter for charecter in n]]
        final_number.reverse()
        return final_number


print(AddTwoNumbers._add([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]))
