# Last updated: 6/18/2025, 11:49:21 PM
class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 1
        rec = nums[0]
        for num in nums:
            if num - rec > k:
                ans += 1
                rec = num
        return ans