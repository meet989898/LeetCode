class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        
        factorial_results = {1: 1}
        seen_sub_groups = set()
        tiles = sorted(tiles)

        ans = 0

        def factorial(n):
            if n in factorial_results: return factorial_results[n]
            factorial_results[n] = n * factorial(n - 1)
            return factorial_results[n]
        
        def counter(arr):
            # I like to make my own counter just to show I can
            temp = {}
            for x in arr:
                temp[x] = temp.get(x, 0) + 1
            return temp 
    
        def arrangements_with_duplicates(letter_counts):
            k = sum(letter_counts.values())
            duplicates = [x for x in letter_counts.values() if x > 1]
            temp = factorial(k)
            for x in duplicates:
                temp //= factorial(x)
            return temp

        for i in range(1, len(tiles) + 1):
            for comb in itertools.combinations(tiles, i):
                if comb in seen_sub_groups:
                    continue
                ans += arrangements_with_duplicates(counter(comb))
                seen_sub_groups.add(comb)
        
        return ans