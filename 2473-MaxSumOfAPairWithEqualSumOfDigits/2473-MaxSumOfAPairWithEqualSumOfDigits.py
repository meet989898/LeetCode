# Last updated: 10/7/2025, 10:28:35 AM
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        
        valid = {}

        result = -1

        for num in nums:
            str_num = str(num)
            sums = 0

            for c in str_num:
                sums += int(c)
            
            if sums not in valid:
                valid[sums] = num
            
            else:
                result = max(result, valid[sums] + num)

                valid[sums] = max(valid[sums], num)
        
        return result