from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        # print(res)

        stack = []

        for i, temp in enumerate(temperatures):
            # print(i, temp)
            while stack and temp > temperatures[stack[-1]]:
                position = stack.pop()
                # print(position)
                res[position] = i - position

            stack.append(i)

        return res


sol = Solution()
print(sol.dailyTemperatures([73,74,75,71,69,72,76,73]))
