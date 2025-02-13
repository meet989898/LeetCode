class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(heap:=[n for n in nums if n < k])
        ops = 0
        while len(heap) > 1:
            ops += 1
            x = 2 * heappop(heap) + heappop(heap)
            if x < k:
                heappush(heap, x)
            else:
                break

        return ops + (len(heap) + 1) // 2