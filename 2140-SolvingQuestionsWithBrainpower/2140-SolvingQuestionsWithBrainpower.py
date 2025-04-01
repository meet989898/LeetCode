# Last updated: 4/1/2025, 10:34:23 AM
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = [0] * len(questions)
        for i in range(len(questions) - 1, -1, -1):
            index = i + questions[i][1] + 1
            if index < len(questions):
                dp[i] = dp[index] + questions[i][0]
            else:
                dp[i] = questions[i][0]
            if i < len(questions) - 1:
                dp[i] = max(dp[i + 1], dp[i])
        return dp[0]