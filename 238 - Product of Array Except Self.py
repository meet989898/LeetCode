from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        listresult = []
        for index, num in enumerate(nums):
            multiplier = 1
            for index2, num2 in enumerate(nums):
                if index == index2:
                    continue
                else:
                    multiplier = multiplier * num2
            listresult.append(multiplier)
        return listresult


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res


sol = Solution()
nums = [1,2,3,4]
print(sol.productExceptSelf(nums))