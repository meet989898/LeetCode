# Last updated: 10/7/2025, 10:27:40 AM
class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        
        result = 0

        for x in range(len(words)):
            for y in range(x+1, len(words)):
                if self.isPrefixAndSuffix(words[x], words[y]):
                    result += 1

        return result
    

    def isPrefixAndSuffix(self, str1, str2):
        if len(str1) > len(str2):
            return False
        
        if str1 == str2[:len(str1)] and str1 == str2[-len(str1):]:
            return True
        
        return False