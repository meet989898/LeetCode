# Last updated: 9/15/2025, 11:49:37 AM
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split()

        broken = set()
        for c in brokenLetters:
            broken.add(c)


        #print(words)

        result = 0

        for word in words:
            flag  = True
            for c in word:
                if c in broken:
                    flag = False
                    break
            
            if flag:
                result += 1

        return result