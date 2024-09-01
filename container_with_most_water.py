from typing import List


class Solution:
    def maxArea(height: List[int]) -> int:
        max_area = 0
        for i, j in enumerate(height):
            for m, n in enumerate(height[i + 1:]):
                area = min(j, n) * (m + 1)

                if area > max_area:
                    max_area = area

        return max_area

        # two_index = []
        # for i in range(len(height)):
        #     for j in height[i + 1:]:
        #         two_index.append((height[i], j))
        # max_area = 0

        # for (x, y) in two_index:
        #     if x == y:
        #         position = [m for m, n in enumerate(height) if n == x]
        #         area = x * (position[1] - position[0])
        #     else:
        #         area = min(x, y) * abs(height.index(y) - height.index(x))

        #     print(area)
        #     if area > max_area:
        #         max_area = area

        # return max_area


msx_area = Solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
print(msx_area)
