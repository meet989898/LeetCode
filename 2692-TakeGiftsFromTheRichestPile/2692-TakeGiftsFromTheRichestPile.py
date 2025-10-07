# Last updated: 10/7/2025, 10:28:11 AM
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        nums = [-num for num in gifts]
        heapify(nums)
        
        while k:
            tmp = math.isqrt(-heappop(nums))
            heappush(nums, -tmp)
            k -= 1
            
        return -sum(nums)
        
       
        