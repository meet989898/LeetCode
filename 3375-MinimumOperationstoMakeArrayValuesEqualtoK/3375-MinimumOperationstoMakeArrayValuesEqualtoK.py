# Last updated: 4/9/2025, 12:05:54 AM
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        for num in nums:
            if num < k:
                return -1
        
        nums = set(nums)

        result = len(nums) - 1 if k in nums else len(nums)

        return result