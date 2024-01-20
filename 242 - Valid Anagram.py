class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            listS = list(s)
            listT = list(t)
            listS.sort()
            listT.sort()
            if listS == listT:
                return True
        return False

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT

s = "nagaram"
t = "anagram"
sol = Solution()
print(sol.isAnagram(s, t))
