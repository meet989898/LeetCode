class Solution:
    def isPalindrome(self, x: int) -> bool:

        nums = str(x)

        if nums == nums[::-1]:
            return True
        else:
            return False