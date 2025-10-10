# Last updated: 10/9/2025, 9:44:18 PM
# go in reverse
class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        
        n = len(energy)

        res = -inf

        for i in range(n - k, n):
            cur = 0
            j = i
            while j >= 0:

                cur += energy[j]
                res = max(res, cur)

                j -= k
            
            
        
        return res

