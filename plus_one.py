from __future__ import annotations

def plusone(digits: list[int]) -> list[int]:
    number_of_digits = len(digits)
    number_obtained = 0
    for posi, digit in enumerate(digits):
        power = 10 ** (number_of_digits - posi-1)
        number_obtained += digit * power
    
    add_one = number_obtained + 1
    return list(map(int, str(add_one)))


print(plusone([4, 3, 2, 1]))



