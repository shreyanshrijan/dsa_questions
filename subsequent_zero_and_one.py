def subsequent_zero_and_one(x: list[int]) -> int:
    left = 0
    right = 1
    counter = 0
    max_length = 0

    while right < len(x):
        if x[left] != x[right]:
            counter += 1

            if counter >= max_length:
                max_length = counter

        else:
            counter = 0

        left += 1
        right += 1
    if max_length == 0:
        return max_length

    return max_length + 1


a = subsequent_zero_and_one([1, 1, 1, 1, 1, 1, 1])
print(a)
