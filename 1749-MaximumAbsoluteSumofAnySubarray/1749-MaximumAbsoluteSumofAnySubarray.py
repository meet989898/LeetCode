    def maxAbsoluteSum(self, nums: List[int]) -> int:
        pos_running_sum = neg_running_sum = max_abs_sum = 0
        for num in nums:
            pos_running_sum, neg_running_sum = max(pos_running_sum + num, num), min(neg_running_sum + num, num)
            max_abs_sum = max(max_abs_sum, pos_running_sum, -neg_running_sum)
        return max_abs_sum