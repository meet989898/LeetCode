from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = {}  # The number -> occurrences
        final = []
        for num in nums:
            if num not in result:
                result[num] = 1
            else:
                result[num] += 1
        print(result)
        occurrences = list(result.values())
        occurrences.sort()



class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

        # O(n)

sol = Solution()
nums = [1, 1, 1, 2, 2, 3]
k = 2
print(sol.topKFrequent(nums, k))
