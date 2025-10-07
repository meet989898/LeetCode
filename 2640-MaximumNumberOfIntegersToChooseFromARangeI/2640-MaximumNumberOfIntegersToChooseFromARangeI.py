# Last updated: 10/7/2025, 10:28:17 AM
class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        # Conver the list to set for easy checking
        banned = set(banned)

        # Keep track of the total sum currently and the total integers encountered
        total = 0
        max_ints = 0

        # Iterate through all the numbers in the range
        for num in range(1, n+1):

            # Skip the numbers in the banned set
            if num in banned:
                continue

            # If the sum is going to exceed the maxsum we dont need to go further
            if total + num > maxSum:
                break

            # If the conditions before are satisfied, we use this integer
            max_ints += 1
            total += num

        # Return the final answer
        return max_ints