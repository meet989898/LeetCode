# Last updated: 9/15/2025, 11:50:52 AM
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        counter = 0
        for word in text.split():
            for letter in word:
                if letter in brokenLetters:
                    counter+=1
                    break
        return len(text.split())-counter
        