class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # If length of string is 0, return 0
        if len(s) == 0:
            return 0

        # Make a hashset of the characters seen
        char_set = set()

        # Initialize the pointers
        left, right = 0, 1

        # Keep track of the length of the longest string
        longest_string = 0

        # Iterate while there are more characters left to check
        while right < len(s):
            print(char_set)
            # If character is not seen before, add it to set and increase the length
            if s[right] not in char_set:
                char_set.add(s[right])
                longest_string = max(longest_string, right - left + 1)
                right += 1

            # If seen before delete the substring till the repeat character is deleted
            else:
                while s[right] in char_set:
                    char_set.remove(s[left])
                    left += 1

        # Return the required length of the longest substring
        return longest_string


sol = Solution()
string = "abcabcbb"
print(sol.lengthOfLongestSubstring(string))