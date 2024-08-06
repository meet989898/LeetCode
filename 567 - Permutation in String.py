class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # Check if the given strings are valid
        if len(s1) > len(s2):
            return False

        # Maintain a dictionary for character counts of s1
        value_of_s1 = {}
        for c in s1:
            if c in value_of_s1:
                value_of_s1[c] += 1
            else:
                value_of_s1[c] = 1

        # Do the similar for the same window size in s2
        value_of_s2 = {}

        # Check the first window directly
        first_string_check = s2[:len(s1)]
        for c in first_string_check:
            if c in value_of_s2:
                value_of_s2[c] += 1
            else:
                value_of_s2[c] = 1
        if value_of_s1 == value_of_s2:
            return True

        # If solution not found continue to other characters
        else:

            # Start from the next window
            left, right = 1, len(s1)

            # Iterate to the end
            while right < len(s2):

                # Update the dictionary counts
                value_of_s2[s2[left-1]] -= 1
                value_of_s2[s2[right]] = 1 + value_of_s2.get(s2[right], 0)

                # If the character reaches 0 count, remove it
                if value_of_s2[s2[left-1]] == 0:
                    del value_of_s2[s2[left-1]]

                # Check for a dictionary match
                if value_of_s2 == value_of_s1:
                    return True

                # Shift the window right
                left += 1
                right += 1

            # Match never found
            return False

        # Neetcode solution - done using lists
        # if len(s1) > len(s2):
        #     return False
        #
        # s1Count, s2Count = [0] * 26, [0] * 26
        # for i in range(len(s1)):
        #     s1Count[ord(s1[i]) - ord("a")] += 1
        #     s2Count[ord(s2[i]) - ord("a")] += 1
        #
        # matches = 0
        # for i in range(26):
        #     matches += 1 if s1Count[i] == s2Count[i] else 0
        #
        # l = 0
        # for r in range(len(s1), len(s2)):
        #     if matches == 26:
        #         return True
        #
        #     index = ord(s2[r]) - ord("a")
        #     s2Count[index] += 1
        #     if s1Count[index] == s2Count[index]:
        #         matches += 1
        #     elif s1Count[index] + 1 == s2Count[index]:
        #         matches -= 1
        #
        #     index = ord(s2[l]) - ord("a")
        #     s2Count[index] -= 1
        #     if s1Count[index] == s2Count[index]:
        #         matches += 1
        #     elif s1Count[index] - 1 == s2Count[index]:
        #         matches -= 1
        #     l += 1
        # return matches == 26


sol = Solution()
s1 = "abc"
s2 = "ccccbbbbaaaa"
print(sol.checkInclusion(s1, s2))