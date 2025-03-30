# Last updated: 3/30/2025, 3:40:16 PM
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        partition_sizes = []
        last_occurrence = [0] * 26
        first_occurrence = [-1] * 26

        partition_start, partition_end = 0, 0

        # Store the last occurrence index of each character
        for i, char in enumerate(s):
            last_occurrence[ord(char) - ord("a")] = i

        for i, char in enumerate(s):
            index = ord(char) - ord("a")

            # Store the first occurrence index of each character (if not set)
            if first_occurrence[index] == -1:
                first_occurrence[index] = i

            # If we find a new partition start
            if partition_end < first_occurrence[index]:
                partition_sizes.append(partition_end - partition_start + 1)
                partition_start = i
                partition_end = i

            # Update partition end boundary
            partition_end = max(partition_end, last_occurrence[index])

        # Add the last partition if it exists
        if partition_end - partition_start + 1 > 0:
            partition_sizes.append(partition_end - partition_start + 1)

        return partition_sizes