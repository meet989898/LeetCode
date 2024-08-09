from typing import List


class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:

        # Predefine the directions
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # Initialize the final array with the start point
        result = [[rStart, cStart]]

        # Keep track of the directions
        i = 0

        # Increase the distance travel every two turns
        steps = 1

        # Run the loop till all cells are visited
        total_cells = rows * cols
        while len(result) < total_cells:

            # Take two turns before increasing travel distance
            for _ in range(2):

                # New direction to use
                dr, dc = directions[i]

                # Travel for a certain number of valid blocks
                for _ in range(steps):

                    # Get the new coordinates to travel to
                    rStart, cStart = rStart + dr, cStart + dc

                    # Only visit if it is a cell in the grid
                    if 0 <= rStart < rows and 0 <= cStart < cols:
                        result.append([rStart, cStart])

                # Change the direction
                i = (i + 1) % 4

            # Increase the travel distance
            steps += 1

        # Return the required result
        return result



sol = Solution()
rows = 5
cols = 6
rStart = 1
cStart = 4

print(sol.spiralMatrixIII(rows, cols, rStart, cStart))