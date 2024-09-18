from typing import List


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1_list = s1.split()
        s2_list = s2.split()

        charset = {}

        result = []

        for word in s1_list:
            charset[word] = charset.get(word, 0) + 1

        for word in s2_list:
            charset[word] = charset.get(word, 0) + 1

        for key, value in charset.items():
            if value == 1:
                result.append(key)

        return result


sol = Solution()
s1 = "this apple is sweet"
s2 = "this apple is sour"
print(sol.uncommonFromSentences(s1, s2))