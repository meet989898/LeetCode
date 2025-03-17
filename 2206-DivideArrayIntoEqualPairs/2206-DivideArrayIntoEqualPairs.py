class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        charCount = {}

        for num in nums:
            charCount[num] = charCount.get(num, 0) + 1
        
        for num, freq in charCount.items():
            if freq % 2 != 0:
                return False
        
        return True