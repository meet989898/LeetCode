from typing import List


class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)

        total = 0
        max_ints = 0
        for num in range(1, n+1):
            if num in banned:
                continue

            if total + num > maxSum:
                break

            # print(num)
            max_ints += 1
            total += num

        return max_ints






solu = Solution()
banned = [1,6,5]
n = 5
maxSum = 6
print(solu.maxCount(banned, n, maxSum))
