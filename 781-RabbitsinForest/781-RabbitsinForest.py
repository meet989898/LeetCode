# Last updated: 4/20/2025, 4:55:44 PM
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        mpp = Counter(answers)
        total = 0
        for x in mpp:
            total += ceil(float(mpp[x]) / (x + 1)) * (x + 1)
        return int(total)