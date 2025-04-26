# Last updated: 4/25/2025, 11:37:39 PM
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        count = 0
        start = -1
        mini = -1
        maxi = -1
        for i in range(len(nums)):
            if nums[i] < minK or nums[i] > maxK:
                start = i
            if nums[i] == maxK:
                maxi = i
            if nums[i] == minK:
                mini = i
            valid = max(0, min(mini, maxi) - start)
            count += valid
        return count