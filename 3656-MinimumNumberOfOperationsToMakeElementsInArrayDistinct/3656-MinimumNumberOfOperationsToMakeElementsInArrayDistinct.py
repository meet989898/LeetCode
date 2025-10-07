# Last updated: 10/7/2025, 10:27:19 AM
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        seen = set()
        for i in range(len(nums) - 1,  -1, -1):
            if nums[i] in seen:
                return i // 3 + 1
            seen.add(nums[i])
        return 0