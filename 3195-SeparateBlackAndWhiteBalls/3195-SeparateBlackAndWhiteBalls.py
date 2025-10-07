# Last updated: 10/7/2025, 10:27:48 AM
class Solution:
    def minimumSteps(self, s: str) -> int:
        
        ones = 0
        res = 0

        for c in s:
            if c == "0":
                res += ones
            else:
                ones += 1
        
        return res