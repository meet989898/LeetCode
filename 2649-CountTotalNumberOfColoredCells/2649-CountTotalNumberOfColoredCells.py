# Last updated: 10/7/2025, 10:28:15 AM
class Solution:
    def coloredCells(self, n: int) -> int:
        return 1 + n * (n - 1) * 2