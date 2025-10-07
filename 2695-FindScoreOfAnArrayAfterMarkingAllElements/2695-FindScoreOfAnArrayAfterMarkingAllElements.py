# Last updated: 10/7/2025, 10:28:10 AM
class Solution:
    def findScore(self, nums: List[int]) -> int:
        n, score, seen = len(nums), 0, set()

        queue = sorted(enumerate(nums), key = lambda x: (x[1],x[0]))

        for idx, num in queue:
            if idx in seen: continue

            score+= num
            
            seen.add(idx)
            if idx > 0  : seen.add(idx-1)
            if idx < n-1: seen.add(idx+1) 
            
        return score