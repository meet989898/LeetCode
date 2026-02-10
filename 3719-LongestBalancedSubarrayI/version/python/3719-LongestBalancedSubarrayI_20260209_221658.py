# Last updated: 2/9/2026, 10:16:58 PM
1class Solution:
2    def longestBalanced(self, nums: List[int]) -> int:
3        max_len = 0
4
5        for i in range(len(nums)):
6            odd = {}
7            even = {}
8
9            for j in range(i, len(nums)):
10                if nums[j] & 1:
11                    odd[nums[j]] = odd.get(nums[j], 0) + 1
12                else:
13                    even[nums[j]] = even.get(nums[j], 0) + 1
14
15                if len(odd) == len(even):
16                    max_len = max(max_len, j - i + 1)
17
18        return max_len