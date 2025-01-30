from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left, right = 0, len(nums) - 1

        while left <= right:

            mid = right - left // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] > target:
                right = mid - 1

            else:
                left = mid + 1

        return -1


sol = Solution()
nums = [-1,0,3,5,9,12]
target = 9
print(sol.search(nums, target))