class Solution:
    def getLucky(self, s: str, k: int) -> int:
        result = ''

        for char in s:
            value = ord(char) - ord('a')
            result += str(value + 1)

        for _ in range(k):
            new_num = 0
            for num in result:
                new_num += int(num)
            result = str(new_num)

        return int(result)

sol = Solution()
s = "iiii"
k = 1
print(sol.getLucky(s, k))