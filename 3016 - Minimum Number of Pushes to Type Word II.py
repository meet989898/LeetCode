class Solution:
    def minimumPushes(self, word: str) -> int:

        # If the word is smaller than the amount of numbers, return word length
        if len(word) <= 8:
            return len(word)

        # Maintain a dictionary of character counts
        char_count = {}
        for char in word:
            char_count[char] = 1 + char_count.get(char, 0)

        # Sort the characters by their count
        char_count = sorted(char_count.items(), key=lambda x: x[1], reverse=True)

        # Make list of lists to store the characters
        num_assignments = [[] for _ in range(8)]

        # Initialize the final result
        button_pushes = 0

        # Iterate through the character in order of count
        for index, item in enumerate(char_count):
            char, count = item

            # Find the index to assign it to and add it to that list
            number_assign = (index % 8)
            num_assignments[number_assign].append(char)

            # According to the position on that list, calculate the button pushes
            button_pushes += len(num_assignments[number_assign]) * count

        # Return the total button pushes
        return button_pushes


sol = Solution()
input = "aabbccddeeffgghhiiiiii"
print(sol.minimumPushes(input))