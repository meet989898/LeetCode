# Last updated: 2/2/2026, 10:33:48 PM
1class Solution:
2    def isTrionic(self, nums: List[int]) -> bool:
3        n = len(nums)
4        i = 1
5
6        while i < n and nums[i - 1] < nums[i]:
7            i += 1
8        p = i - 1
9
10        while i < n and nums[i - 1] > nums[i]:
11            i += 1
12        q = i - 1
13
14        while i < n and nums[i - 1] < nums[i]:
15            i += 1
16        flag = i - 1
17
18        return (p != 0) and (q != p) and (flag == n - 1 and flag != q)