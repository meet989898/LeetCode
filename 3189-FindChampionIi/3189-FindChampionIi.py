# Last updated: 10/7/2025, 10:27:49 AM
class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        isUndefeated = [True] * n
        
        for winner, loser in edges:
            isUndefeated[loser] = False
            
        champion = -1
        championCount = 0
        
        for team in range(n):
            if isUndefeated[team]:
                champion = team
                championCount += 1
                
        if championCount == 1:
            return champion
            
        return -1