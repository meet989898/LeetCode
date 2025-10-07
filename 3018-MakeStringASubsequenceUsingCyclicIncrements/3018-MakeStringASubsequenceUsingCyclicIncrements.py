# Last updated: 10/7/2025, 10:27:54 AM
class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        i = 0
        j = 0
        
        def less_char(char):
            return 'z' if char == 'a' else chr(ord(char) - 1)
        
        while i < len(str1) and j < len(str2):
            if str1[i] == less_char(str2[j]) or str1[i] == str2[j]:
                j += 1
            i += 1
        
        return j == len(str2)