# Last updated: 2/7/2026, 5:07:24 PM
1class Solution:
2    def minimumDeletions(self, s: str) -> int:
3        char_stack = []
4        delete_count = 0
5
6        # Iterate through each character in the string
7        for char in s:
8            # If stack is not empty, top of stack is 'b',
9            # and current char is 'a'
10            if char_stack and char_stack[-1] == "b" and char == "a":
11                char_stack.pop()  # Remove 'b' from stack
12                delete_count += 1  # Increment deletion count
13            else:
14                char_stack.append(char)  # Append current character to stack
15
16        return delete_count