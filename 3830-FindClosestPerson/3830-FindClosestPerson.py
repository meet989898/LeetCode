# Last updated: 10/7/2025, 10:27:15 AM
class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        
        per1 = abs(x-z)
        per2 = abs(y-z)

        if per1 > per2:
            return 2
        elif per1 < per2:
            return 1
        
        return 0