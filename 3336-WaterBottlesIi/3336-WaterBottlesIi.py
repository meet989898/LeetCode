# Last updated: 10/7/2025, 10:27:38 AM
class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        empty = numBottles
        while empty >= numExchange:
            ans += 1
            empty -= numExchange - 1
            numExchange += 1
        return ans