# Last updated: 2/3/2026, 11:44:28 PM
1class Solution:
2    def maxSumTrionic(self, nums: List[int]) -> int:
3        n = len(nums)
4        ans = float("-inf")
5        i = 0
6
7        while i < n:
8            j = i + 1
9            res = 0
10
11            # first segment: increasing segment
12            while j < n and nums[j - 1] < nums[j]:
13                j += 1
14            p = j - 1
15
16            if p == i:  # 没有有效的increasing segment
17                i += 1
18                continue
19
20            # second segment: decreasing segment
21            res += nums[p] + nums[p - 1]
22            while j < n and nums[j - 1] > nums[j]:
23                res += nums[j]
24                j += 1
25            q = j - 1
26
27            if q == p or q == n - 1 or (j < n and nums[j] <= nums[q]):
28                i = q
29                continue
30
31            # third segment: increasing segment
32            res += nums[q + 1]
33
34            # find the maximum sum of the third segment
35            max_sum = 0
36            curr_sum = 0
37            k = q + 2
38            while k < n and nums[k] > nums[k - 1]:
39                curr_sum += nums[k]
40                max_sum = max(max_sum, curr_sum)
41                k += 1
42            res += max_sum
43
44            # find the maximum sum of the first segment
45            max_sum = 0
46            curr_sum = 0
47            for k in range(p - 2, i - 1, -1):
48                curr_sum += nums[k]
49                max_sum = max(max_sum, curr_sum)
50            res += max_sum
51
52            # update answer
53            ans = max(ans, res)
54            i = q
55
56        return ans