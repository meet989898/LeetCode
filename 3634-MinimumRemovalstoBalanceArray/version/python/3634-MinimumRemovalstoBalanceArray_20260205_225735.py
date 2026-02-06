# Last updated: 2/5/2026, 10:57:35 PM
1class Solution:
2    def minRemoval(self, nums: List[int], k: int) -> int:
3        nums.sort()
4        i = 0
5        max_len = 0
6        
7        for j in range(len(nums)):
8            while nums[j] > nums[i] * k:
9                i += 1
10            max_len = max(max_len, j - i + 1)
11            
12        return len(nums) - max_len