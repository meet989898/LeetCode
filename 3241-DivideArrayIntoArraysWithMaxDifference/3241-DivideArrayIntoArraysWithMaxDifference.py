# Last updated: 10/7/2025, 10:27:45 AM
class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:

        res = []

        n = len(nums)
        
        nums.sort()

        for i in range(0, n, 3):
            num1, num2, num3 = nums[i], nums[i + 1], nums[i + 2]

            if num3 - num1 <= k:
                res.append([num1, num2, num3])
            else:
                return []
        
        return res

        