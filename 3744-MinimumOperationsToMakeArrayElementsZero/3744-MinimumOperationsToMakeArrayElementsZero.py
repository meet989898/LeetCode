# Last updated: 10/7/2025, 10:27:15 AM
class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:

        def get(l, r):

            L = S = 1
            steps = 0
            
            while (L<=r):
                R = 4*L-1

                start = max(L, l)
                end = min(R, r)

                if start <= end:

                    steps += (end - start + 1) * S

                S += 1
                L *= 4
            
            return steps

        result = 0

        for query in queries:
            l, r = query[0], query[1]

            steps = get(l, r)

            result += (steps+1)//2
        
        return result