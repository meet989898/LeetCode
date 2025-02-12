class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        
        valid = defaultdict(list)

        for i, num in enumerate(nums):
            str_num = str(num)
            sums = 0

            for c in str_num:
                sums += int(c)

            valid[sums].append(num)
        
        result = 0
        for sums, numbers in valid.items():
            if len(numbers) > 1:
                numbers.sort(reverse=True)

                result = max(result, numbers[0] + numbers[1])
        
        return result if result > 0 else -1
