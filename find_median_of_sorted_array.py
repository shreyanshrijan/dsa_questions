from typing import List


class Solution:
    def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
        merged_array = nums1 + nums2
        merged_array.sort()

        if (len(merged_array) % 2) != 0:
            return merged_array[int(len(merged_array)/2)]
        x = (
            merged_array[len(merged_array)/2 - 1]
            + merged_array[len(merged_array)/2]
        )

        return x/2


print(Solution.findMedianSortedArrays([1, 3], [2]))
