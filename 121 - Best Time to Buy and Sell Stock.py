from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize pointers
        max_profit = 0
        left, right = 0, 1

        # Run the loop till we check all the prices
        while right < len(prices):

            # Only check profit if price increases
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)

            # A new low price point found
            else:
                left = right

            # Keep going right regardless
            right += 1

        # Return the answer
        return max_profit


sol = Solution()
numbers = [7,1,5,3,6,4]
print(sol.maxProfit(numbers))