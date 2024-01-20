from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in nums:
            if num - 1 in numSet:
                continue
            length = 0
            while num + length in numSet:
                length += 1
            longest = max(longest, length)
        return longest




sol = Solution()
nums = [100,4,200,1,3,2]
print(sol.longestConsecutive(nums))