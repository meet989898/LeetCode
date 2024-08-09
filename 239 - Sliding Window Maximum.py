import collections
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        # Handle edge cases or simple cases
        if k >= len(nums):
            return [max(nums)]

        # Initialize the result array
        result = []

        # Use a queue to keep track of high numbers
        queue = collections.deque()

        # Add the first element by default
        queue.append(0)

        # Create and check the first window
        for i in range(1, k):

            # Pop smaller values from the left before adding new numbers
            while queue and nums[queue[-1]] <= nums[i]:
                queue.pop()
            queue.append(i)

        # This is the answer to the first window
        result.append(nums[queue[0]])

        # Shift the window to the right
        left, right = 1, k

        # Keep doing the above steps till we complete the list
        while right < len(nums):

            # Pop smaller values from the left before adding new numbers
            while queue and nums[queue[-1]] <= nums[right]:
                queue.pop()
            queue.append(right)

            # Remove the largest number only if it is gone outside the window
            if left > queue[0]:
                queue.popleft()

            # Get the current biggest number
            result.append(nums[queue[0]])

            # Shift to the right
            left += 1
            right += 1

        # Return the final populated array
        return result



sol = Solution()
nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(sol.maxSlidingWindow(nums, k))