import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = []
        checked = {}
        for i in range(len(strs)):
            if strs[i] in checked:

                continue
            else:
                newwordlist = []
                checked[strs[i]] = i
                newwordlist.append(strs[i])
                for j in range(i + 1, len(strs)):
                    if strs[i] == strs[j]:
                        newwordlist.append(strs[j])
                    elif strs[j] not in checked and self.isAnagram(strs[i], strs[j]):
                        checked[strs[j]] = j
                        newwordlist.append(strs[j])
                grouped.append(newwordlist)

        return grouped
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
        return ans.values()


class Solution:
    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #     agent = AnagramsFinder(strs)
    #     return agent.run()

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_book = defaultdict(list)
        for word in strs:  # O(n)
            anagrams_book["".join(sorted(word))].append(word)  # O(xlogx + x)
        return anagrams_book.values()

sol = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
print(sol.groupAnagrams(strs))