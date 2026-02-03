# Last updated: 2/2/2026, 10:34:12 PM
1class Solution:
2    def isTrionic(self, nums: List[int]) -> bool:
3        n = len(nums)
4        if nums[0] >= nums[1]:
5            return False
6
7        count = 1
8        for i in range(2, n):
9            if nums[i - 1] == nums[i]:
10                return False
11            if (nums[i - 2] - nums[i - 1]) * (nums[i - 1] - nums[i]) < 0:
12                count += 1
13
14        return count == 3