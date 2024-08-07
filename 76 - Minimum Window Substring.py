class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # If the sting length are invalid, return empty string
        if len(t) > len(s): return ""

        # Keep a count of characters seen in string t
        t_char_count = {}

        # Keep a boolean dictionary to track the matches made
        matches = {}

        # Iterate through string t and populate the dictionaries
        for char in t:
            t_char_count[char] = t_char_count.get(char, 0) + 1
            matches[char] = False

        # Initialize the pointers for a sliding window
        left, right = 0, len(t) - 1

        # Similarly keep track of string s character counts
        s_char_count = {}

        # Keep a track of the number of matches made and needed
        matches_made = 0
        total_matches = len(t_char_count)

        # Check the first window directly
        first_string_check = s[:len(t)]
        for c in first_string_check:
            if c in t_char_count:
                if c in s_char_count:
                    s_char_count[c] += 1
                else:
                    s_char_count[c] = 1

        # Update the matches and see if it matched
        for char, count in t_char_count.items():
            if char in s_char_count and s_char_count[char] >= count:
                matches[char] = True
                matches_made += 1

        # Return the answer if match already made
        if matches_made == total_matches:
            return first_string_check

        # Initialize the comparison variables
        min_substring_length = float('inf')
        min_substring = ""
        right += 1

        # Iterate through string s
        while right < len(s):

            # If the new character is one we are interested in
            if s[right] in t_char_count:
                s_char_count[s[right]] = s_char_count.get(s[right], 0) + 1

                # Match it if match not already made
                if s_char_count[s[right]] >= t_char_count[s[right]] and not matches[s[right]]:
                    matches[s[right]] = True
                    matches_made += 1

                # Discard the duplicates and non-needed characters from the left
                while ((s_char_count.get(s[left], 0) > t_char_count.get(s[left], 0) or
                       s[left] not in t_char_count) and
                       left <= right):
                    if s[left] in t_char_count:
                        s_char_count[s[left]] -= 1
                    left += 1

                # Check if the string is shorter
                if matches_made == total_matches:
                    if len(s[left:right + 1]) < min_substring_length:
                        min_substring_length = len(s[left:right + 1])
                        min_substring = s[left:right + 1]

            # Keep updating the right pointer to keep going
            right += 1

        # Return the string to be used
        return min_substring

    # Neetcode solution - Similar logic, uses a little less time and code is shorter
    # if t == "":
    #     return ""
    #
    # countT, window = {}, {}
    # for c in t:
    #     countT[c] = 1 + countT.get(c, 0)
    #
    # have, need = 0, len(countT)
    # res, resLen = [-1, -1], float("infinity")
    # l = 0
    # for r in range(len(s)):
    #     c = s[r]
    #     window[c] = 1 + window.get(c, 0)
    #
    #     if c in countT and window[c] == countT[c]:
    #         have += 1
    #
    #     while have == need:
    #         # update our result
    #         if (r - l + 1) < resLen:
    #             res = [l, r]
    #             resLen = r - l + 1
    #         # pop from the left of our window
    #         window[s[l]] -= 1
    #         if s[l] in countT and window[s[l]] < countT[s[l]]:
    #             have -= 1
    #         l += 1
    # l, r = res
    # return s[l: r + 1] if resLen != float("infinity") else ""


sol = Solution()
s1 = "ADOBECODEBANC"
s2 = "ABC"
print(sol.minWindow(s1, s2))