from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        numset = {}
        for i in range(9, -1, -1):
            # numset = {'9': 0, '8': 0, '7': 0, '6': 0, '5': 0, '4': 0, '3': 0, '2': 0, '1': 0, '0': 0}
            pass


        for num in nums:
            num = str(num)
            for char in num:
                numset[char] += 1

        result = ''

        for key, value in numset.items():
            for _ in range(value):
                result += key

        return result




sol = Solution()
nums = [3,30,34,5,9]
print(sol.largestNumber(nums))