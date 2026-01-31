# Last updated: 1/31/2026, 4:18:31 PM
# break it instantly on the first find, since it is sorted. if not sorted check and compare every letter
1class Solution:
2    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
3        res = letters[0]
4
5        for ch in letters:
6            if ch > target:
7                res = ch
8                break
9
10        return res