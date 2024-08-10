import collections


class Solution:
    def isValid(self, s: str) -> bool:

        # Keep a map of the open and close brackets
        char_close = {')': '(', '}': '{', ']': '['}

        # Use a queue as a stack
        q = collections.deque()

        # Go through each character
        for char in s:

            # If the character is an opening character, add to the stack
            if char not in char_close:
                q.append(char)

            # If it is a closing character, check for opening characters
            else:

                # Confirm if the stack is not empty
                if q:

                    # If the closing bracket is misplaced, return False
                    if q.pop() != char_close[char]:
                        return False

                # If empty return False
                else:
                    return False

        # At the end if there are any extra opening brackets left return False
        if q:
            return False

        # Else finally return True
        return True


sol = Solution()
s = "()"
print(sol.isValid(s))