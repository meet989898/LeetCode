# Last updated: 2/11/2026, 11:13:19 PM
1class Solution:
2    def longestBalanced(self, s: str) -> int:
3        n = len(s)
4        res = 0
5        for i in range(n):
6            cnt = defaultdict(int)
7            for j in range(i, n):
8                cnt[s[j]] += 1
9                if len(set(cnt.values())) == 1:
10                    res = max(res, j - i + 1)
11        return res