from typing import List


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        result = []

        if m * n != len(original):
            return result

        for i in range(m):
            new_list = []
            for j in range(n):
                new_list.append(original[(i * n) + j])
            result.append(new_list)

        new_list = None
        return result




sol = Solution()
original = [1,2,3,4]
m = 2
n = 2
print(sol.construct2DArray(original, m, n))