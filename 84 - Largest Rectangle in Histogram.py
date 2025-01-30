from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)

        maxArea = 0
        stack = []
        for index, height in enumerate(heights):
            start = index

            while stack and stack[-1][1] > height:
                i, h = stack.pop()
                maxArea = max(maxArea, h * (index - i))
                start = i

            stack.append((start, height))

        for i, h in stack:
            maxArea = max(maxArea, h * (n - i))

        return maxArea

solu = Solution()

print(solu.largestRectangleArea([2,1,5,6,2,3]))