# Last updated: 1/8/2026, 5:14:14 PM
1class Solution:
2    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
3        memo = {}
4
5        # max dot product of two subsequences starting at i,j
6        def dp(i,j):
7
8            if i == len(nums1) or j == len(nums2):
9                return float("-inf") # if we are passed the boundary, dont pick anything from there.
10
11            if (i,j) in memo:
12                return memo[(i,j)]
13
14            take = nums1[i] * nums2[j]
15            res = max(
16            # take i,j. move forward
17                take + dp(i+1, j+1),
18
19            # take this subsequence and just end.
20                take,
21
22            # skip i: i+1,j
23                dp(i+1,j),
24
25            # skip j: i,j+1
26                dp(i,j+1),
27            )
28
29            memo[(i,j)] = res
30
31            return memo[(i,j)]
32
33        return dp(0,0)