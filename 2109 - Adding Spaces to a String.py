from typing import List


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        space_set = set(spaces)

        result = ""
        for index, char in enumerate(s):

            if index in space_set:
                result += " "

            result += char

        return result




sol = Solution()
s = "LeetcodeHelpsMeLearn"
spaces = [8,13,15]
print(sol.addSpaces(s, spaces))
