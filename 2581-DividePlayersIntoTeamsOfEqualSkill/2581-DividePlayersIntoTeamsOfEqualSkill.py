# Last updated: 10/7/2025, 10:28:23 AM
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:

        # Step 1: Sort the skill array
        skill.sort()
        
        n = len(skill)
        total_skill = skill[0] + skill[-1]  # Required sum for each pair
        chemistry_sum = 0
        
        # Step 2: Pair players using two pointers
        for i in range(n // 2):
            # Check if the sum of current pair matches the required total_skill
            if skill[i] + skill[n - 1 - i] != total_skill:
                return -1  # Invalid configuration, return -1
            # Calculate the chemistry and accumulate the sum
            chemistry_sum += skill[i] * skill[n - 1 - i]

        return chemistry_sum  # Return total chemistry



        

        