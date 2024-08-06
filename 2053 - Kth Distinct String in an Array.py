from typing import List


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:

        char_set = {}

        for string in arr:
            if string in char_set:
                char_set[string] += 1
            else:
                char_set[string] = 1

        valid_strings = []
        for string, count in char_set.items():
            if count == 1:
                valid_strings.append(string)

        if len(valid_strings) >= k:
            return valid_strings[k - 1]
        else:
            return ""


sol = Solution()
input_string = ["d", "b", "c", "b", "c", "a"]
print(sol.kthDistinct(input_string, 2))
