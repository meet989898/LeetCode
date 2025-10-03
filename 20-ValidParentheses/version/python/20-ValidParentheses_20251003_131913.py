# Last updated: 10/3/2025, 1:19:13 PM
class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        pair = {
            "}": "{",
            "]": "[",
            ")": "("
        }

        for c in s:
            if c in ["}", "]", ")"]:
                if not stack or not stack[-1] == pair[c]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(c)
        
        return False if stack else True
        