class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # Initialize the hashmap, pointers and desired variables
        count_of_chars = {}
        left, right = 0, 0
        max_freq = 0
        len_substring = 0

        # Loop till we reach the end of string
        while right < len(s):

            # Check the window length
            window_length = right - left + 1

            # If character is in hashmap then update otherwise add
            if s[right] in count_of_chars:
                count_of_chars[s[right]] += 1
            else:
                count_of_chars[s[right]] = 1

            # Keep track of the max frequency of the hashmap
            max_freq = max(max_freq, count_of_chars[s[right]])

            # If the given string has no more valid points to be converted,
            # we shorten the window from left
            while window_length - max_freq > k:
                count_of_chars[s[left]] -= 1
                left += 1
                window_length -= 1

            # Keep track of the substring formed before shifting right
            len_substring = max(len_substring, window_length)

            # Check the next character
            right += 1

        # Return the desired length
        return len_substring




sol = Solution()
string = "AABABBA"
k = 2
print(sol.characterReplacement(string, k))