# Last updated: 1/31/2026, 4:20:17 PM
# binary search since its a sorted list
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        start = 0
        end = len(letters)

        while start< end:
            mid = (start+end)//2
            if letters[mid] > target:
                end = mid
            else:
                start = mid+1
        if start>= len(letters):
            return letters[0]
        else:
            return letters[start]