# Last updated: 2/1/2026, 11:55:49 PM
1class Solution:
2    def minimumCost(self, nums: List[int]) -> int:
3        nums[1:] = sorted(nums[1:])
4        return sum(nums[:3])