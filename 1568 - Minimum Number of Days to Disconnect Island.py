from typing import List


class Solution:
    def minDays(self, grid: List[List[int]]) -> int:

        # Total rows and columns
        rows, cols = len(grid), len(grid[0])

        # Helper function to count the number of islands at any given point
        def countIslands():

            # Maintain a list of lists to keep track of visited cells
            visited = [[False] * cols for _ in range(rows)]

            # DFS approach to traverse a connected island
            def dfs(row, col):

                # Base conditions
                if 0 > row or row >= rows or 0 > col or col >= cols or grid[row][col] == 0 or visited[row][col]:
                    return

                # Mark the cell as visited
                visited[row][col] = True

                # Iterate through the neighbours
                neighbors = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
                for neighbor in neighbors:
                    dfs(neighbor[0], neighbor[1])

            # Initialize the total islands
            islands = 0

            # Go through the entire grid
            for row in range(rows):
                for col in range(cols):
                    if grid[row][col] == 1 and not visited[row][col]:
                        islands += 1
                        dfs(row, col)

            # Return the number of islands
            return islands

        # Count the number of islands
        islands = countIslands()

        # Base condition to see if the given grid already has more than 1 island
        if islands != 1:
            return 0

        # Go through the entire grid
        for row in range(rows):
            for col in range(cols):

                # Change land to water and check if it disconnects
                if grid[row][col] == 1:
                    grid[row][col] = 0

                    islands = countIslands()

                    if islands != 1:
                        return 1

                    # If not then we try another block
                    grid[row][col] = 1

        # Only 1 day cannot be used. Max 2 days is used
        return 2

        # # Total rows and columns
        # rows, cols = len(grid), len(grid[0])
        #
        # # Helper function to count the number of islands at any given point
        # def countIslands():
        #
        #     # Maintain a list of lists to keep track of visited cells
        #     visited = set()
        #
        #     # DFS approach to traverse a connected island
        #     def dfs(row, col):
        #
        #         # Base conditions
        #         if 0 > row or row >= rows or 0 > col or col >= cols or grid[row][col] == 0 or (row, col) in visited:
        #             return
        #
        #         # Mark the cell as visited
        #         visited.add((row, col))
        #
        #         # Iterate through the neighbours
        #         neighbors = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
        #         for neighbor in neighbors:
        #             dfs(neighbor[0], neighbor[1])
        #
        #     # Initialize the total islands
        #     islands = 0
        #
        #     # Go through the entire grid
        #     for row in range(rows):
        #         for col in range(cols):
        #             if grid[row][col] == 1 and (row, col) not in visited:
        #                 islands += 1
        #                 if islands > 1:
        #                     return islands, visited
        #                 dfs(row, col)
        #
        #     # Return the number of islands
        #     return islands, visited
        #
        # # Count the number of islands
        # islands, visited = countIslands()
        # visited = list(visited)
        #
        # # Base condition to see if the given grid already has more than 1 island
        # if islands != 1:
        #     return 0
        #
        # else:
        #
        #     if len(visited) < 3:
        #         return len(visited)
        #
        #     for coord in visited:
        #         surrounding_land = 0
        #         row, col = coord[0], coord[1]
        #         # Iterate through the neighbours
        #         neighbors = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
        #         top = grid[row - 1][col]
        #         bottom = grid[row + 1][col]
        #         neighbors_found = [False] * 4
        #         for i, neighbor in enumerate(neighbors):
        #             nr, nc = neighbor[0], neighbor[1]
        #             if 0 > nr or nr >= rows or 0 > nc or nc >= cols or grid[nr][nc] == 0:
        #                 continue
        #             # print(nr, nc)
        #             surrounding_land += 1
        #             neighbors_found[i] = True
        #
        #         # print(surrounding_land, row, col)
        #         if surrounding_land == 1:
        #             return 1
        #         elif surrounding_land == 2:
        #             if (neighbors_found[0] and neighbors_found[1]) or (neighbors_found[2] and neighbors_found[3]):
        #                 grid[row][col] = 0
        #                 islands, visited = countIslands()
        #                 if islands != 1:
        #                     return 1
        #                 return 2
        #
        #     return 2






sol = Solution()
# grid = [[0,1,1,0],[0,1,1,0],[0,0,0,0]]
# grid = [[1, 1]]
grid = [[1,1,0,1,1],[1,1,1,1,1],[1,1,0,1,1],[1,1,1,1,1]]
for row in grid:
    print(row)
print(sol.minDays(grid))