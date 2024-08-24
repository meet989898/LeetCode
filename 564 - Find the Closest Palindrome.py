class Solution:
    def nearestPalindromic(self, n: str) -> str:
        step = 1
        n = int(n)
        while True:
            back_num = n - step
            front_num = n + step

            if self.is_palindrome(str(back_num)):
                return str(back_num)

            elif self.is_palindrome(str(front_num)):
                return str(front_num)

            step += 1

    def is_palindrome(self, num: str) -> bool:

        if num == num[::-1]:
            return True

        else:
            return False


sol = Solution()
n = "807045053224792883"
print(sol.nearestPalindromic(n))
