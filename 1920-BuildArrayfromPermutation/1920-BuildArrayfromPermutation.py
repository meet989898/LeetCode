# Last updated: 5/5/2025, 10:49:01 PM
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)

        for i in range(len(nums)):
            ans[i] = nums[nums[i]]
        

        return ans