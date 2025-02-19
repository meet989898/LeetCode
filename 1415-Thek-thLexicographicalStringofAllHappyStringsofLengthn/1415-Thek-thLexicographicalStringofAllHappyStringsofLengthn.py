class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        if k > 3 * (2 ** (n - 1)):
            return ''

        res = []
        self.helper([], n, res)
        return res[k - 1]

    def helper(self, curr, n, res):
        if len(curr) == n:
            res.append(''.join(curr))
            return

        c = curr[-1] if curr else ''
        if c != 'a':
            curr.append('a')
            self.helper(curr, n, res)
            curr.pop()
        if c != 'b':
            curr.append('b')
            self.helper(curr, n, res)
            curr.pop()
        if c != 'c':
            curr.append('c')
            self.helper(curr, n, res)
            curr.pop()