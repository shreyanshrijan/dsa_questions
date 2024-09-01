from __future__ import annotations


class TwoSum:
    def __init__(self, nums: list, target: int) -> tuple[int, int]:
        self.nums = nums
        self.target = target

    def _find_indices(self):
        numMap = {}
        n = len(self.nums)

        for i in range(n):
            complement = self.target - self.nums[i]

            if complement in numMap:
                return [numMap[complement], i]
            numMap[self.nums[i]] = i

        return []


two_sum = TwoSum([2, 7, 11, 15], 26)
print(two_sum._find_indices())
