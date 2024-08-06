from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        total_water = 0
        if len(height) <= 1:
            return 0

        max_left = [0]
        max_left_height = height[0]
        for i in range(1, len(height)):
            max_left.append(max_left_height)

            max_left_height = max(max_left_height, height[i])

        min_right = [0] * len(height)
        min_right_height = height[len(height) - 1]
        for i in range(len(height) - 2, -1, -1):
            min_right[i] = min_right_height

            min_right_height = max(min_right_height, height[i])

        for i in range(len(height)):
            water = min(max_left[i], min_right[i]) - height[i]

            if water > 0:
                total_water += water

        return total_water

    def trap2(self, height: List[int]) -> int:
        print(height)
        total_water = 0
        if len(height) <= 1:
            return 0

        left, right = 0, len(height) - 1
        max_left, max_right = height[left], height[right]

        while left < right:
            left_height = height[left]
            right_height = height[right]

            if left_height <= right_height:
                left += 1
                water = max_left - height[left]

                if water > 0:
                    total_water += water

                max_left = max(max_left, height[left])

            else:

                right -= 1
                water = max_right - height[right]

                if water > 0:
                    total_water += water

                max_right = max(max_right, height[right])

        return total_water


sol = Solution()
numbers = [4,2,0,3,2,5]
print(sol.trap2(numbers))