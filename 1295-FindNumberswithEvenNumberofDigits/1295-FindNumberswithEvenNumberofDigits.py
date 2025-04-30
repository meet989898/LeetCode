# Last updated: 4/30/2025, 7:35:24 PM
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res = 0

        for num in nums:

            if len(str(num)) % 2 == 0:
                res += 1

        return res