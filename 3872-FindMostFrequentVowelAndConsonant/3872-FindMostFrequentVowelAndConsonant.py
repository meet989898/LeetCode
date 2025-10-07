# Last updated: 10/7/2025, 10:27:14 AM
class Solution:
    def maxFreqSum(self, s: str) -> int:
        freq = [0] * 26
        maxVowel, maxConso = 0, 0
        for c in s:
            i = ord(c) - ord('a')
            freq[i] += 1
            if c in 'aeiou':
                maxVowel = max(maxVowel, freq[i])
            else:
                maxConso = max(maxConso, freq[i])
        return maxVowel + maxConso