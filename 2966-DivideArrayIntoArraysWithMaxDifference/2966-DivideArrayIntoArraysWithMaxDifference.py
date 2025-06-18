# Last updated: 6/17/2025, 11:39:05 PM
class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:

        res = []

        n = len(nums)
        
        nums.sort()

        for i in range(0, len(nums), 3):
            num1, num2, num3 = nums[i], nums[i + 1], nums[i + 2]

            if num3 - num1 <= k:
                res.append([num1, num2, num3])
            else:
                return []
        
        return res

        