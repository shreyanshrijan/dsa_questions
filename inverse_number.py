class Solution:
    def reverse(x: int) -> int:
        x_str: list = [i for i in str(x)]
        if x_str[0] == '-':
            negative_value = x_str[0:1]
            digits = x_str[1:]
            digits.reverse()

            x_str = negative_value + digits
        else:
            x_str.reverse()
        reversed_str = "".join(x_str)
        return int(reversed_str)


print(Solution.reverse(x=-123))
