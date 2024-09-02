from typing import List


class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total_chalk = sum(chalk)
        k = k % total_chalk

        for i in range(len(chalk)):
            if chalk[i] > k:
                return i

            k = k - chalk[i]



sol = Solution()
chalk = [3,4,1,2]
k = 25
print(sol.chalkReplacer(chalk, k))