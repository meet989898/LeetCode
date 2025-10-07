# Last updated: 10/7/2025, 10:28:29 AM
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        length = 0
        max_val = 0

        # 1st loop to find the maximum value
        max_val = max(nums)

        # 2nd loop to find the longest contiguous subarray of the maximum value
        count = 0
        for num in nums:
            if num == max_val:
                count += 1
                length = max(length, count)
            else:
                count = 0

        return length