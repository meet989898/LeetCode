from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def pivot():
            l, r = 0, len(nums) - 1

            while l < r:

                m = (l + r) // 2
                if nums[m] > nums[r]:
                    l = m + 1
                else:
                    r = m
            return l

        def binary_search(left, right):

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    return mid

                elif nums[mid] < target:
                    left = mid + 1

                else:
                    right = mid - 1

            return -1

        pivot_index = pivot()
        # print(pivot_index)

        res = binary_search(0, pivot_index - 1)

        if res == -1:
            res = binary_search(pivot_index, len(nums) - 1)

        return res


sol = Solution()
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
print(sol.search(nums, target))
