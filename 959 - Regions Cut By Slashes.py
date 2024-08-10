from typing import List


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:

        # Get the size of the NxN grid
        n = len(grid)

        # Initialize the result
        result = 0

        # Base condition of just a 1x1 grid
        if n == 1:
            if grid[0][0] == ' ':
                return result + 1
            else:
                return result + 2

        # Scale up the small given grid to 3 times the size
        big_rows, big_cols = n * 3, n * 3
        big_grid = [[0 for _ in range(big_cols)] for _ in range(big_rows)]

        # Map the small grid onto the bigger grid
        for row in range(n):
            for col in range(n):
                if grid[row][col] == '\\':
                    big_row, big_col = row * 3, col * 3
                    big_grid[big_row][big_col] = 1
                    big_grid[big_row + 1][big_col + 1] = 1
                    big_grid[big_row + 2][big_col + 2] = 1

                elif grid[row][col] == '/':
                    big_row, big_col = row * 3, col * 3
                    big_grid[big_row][big_col + 2] = 1
                    big_grid[big_row + 1][big_col + 1] = 1
                    big_grid[big_row + 2][big_col] = 1

        # Helper dfs function to traverse the empty cells
        def dfs(r, c):

            # Base conditions
            if 0 > r or r >= big_rows or 0 > c or c >= big_cols or (r, c) in seen or big_grid[r][c] == 1:
                return

            # Add it to visited cells
            seen.add((r, c))

            # Explore the neighbours recursively
            neighbors = [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]
            for neighbor in neighbors:
                r, c = neighbor[0], neighbor[1]
                dfs(r, c)

        # Maintain a hashset to see the visited cells
        seen = set()

        # Go through the entire big grid to check the number of parts
        for row in range(big_rows):
            for col in range(big_cols):
                if (row, col) not in seen and big_grid[row][col] == 0:
                    dfs(row, col)
                    result += 1

        # Return the result
        return result


sol = Solution()
grid = ["/\\","\\/"]
print(sol.regionsBySlashes(grid))