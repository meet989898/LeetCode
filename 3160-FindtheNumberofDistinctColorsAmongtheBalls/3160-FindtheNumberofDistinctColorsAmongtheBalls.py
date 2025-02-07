class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        if len(queries) == 0:
            return 0

        res = []
        colors = {}
        balls = {}

        for ball, color in queries:
            
            if ball in balls:
                colors[balls[ball]] -= 1
                if colors[balls[ball]] == 0:
                    del colors[balls[ball]]

            colors[color] = colors.get(color, 0) + 1
            balls[ball] = color

            res.append(len(colors))
        
        return res



