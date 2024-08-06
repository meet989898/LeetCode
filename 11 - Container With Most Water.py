from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_capacity = 0
        # for i in range(len(height)):
        #     for j in range(i+1, len(height)):
        #         distance = abs(i - j)
        #         height_of_vessel = min(height[i], height[j])
        #
        #         total_volume = distance * height_of_vessel
        #
        #         max_capacity = max(max_capacity, total_volume)
        left, right = 0, len(height) - 1
        while left < right:
            distance = abs(left - right)
            height_of_vessel = min(height[left], height[right])

            total_volume = distance * height_of_vessel
            max_capacity = max(max_capacity, total_volume)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_capacity



sol = Solution()
numbers = [1,8,6,2,5,4,8,3,7]
print(sol.maxArea(numbers))
