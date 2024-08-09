from typing import List


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:

        # Number of rows and columns
        rows = len(grid)
        cols = len(grid[0])

        # Default case of invalid grid
        if rows < 3 or cols < 0:
            return 0

        # Presetting the corner and side coordinates
        corners = [[-1, -1], [1, 1], [1, -1], [-1, 1]]
        sides = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        # Final resulting number of total 3x3 magic squares
        total_magic_squares = 0

        # Check all the cells to see if we see a 5
        for row in range(1, rows-1):
            for col in range(1, cols-1):
                if grid[row][col] == 5:

                    # Check to see if the 3x3 is a valid answer
                    if self.is_valid(corners, sides, row, col, grid):
                        total_magic_squares += 1

        # Return the final required answer
        return total_magic_squares

    # This is a helper function that confirms whether a subgrid is valid
    def is_valid(self, corners, sides, row, col, grid):

        # Hashset to check for seen numbers
        seen_numbers = set()
        seen_numbers.add(5)

        # Check the corner conditions
        for corner in corners:
            number = grid[row + corner[0]][col + corner[1]]
            if number in seen_numbers or number % 2 == 1 or 0 >= number >= 10:
                return False
            seen_numbers.add(number)

        # Check the side conditions
        for side in sides:
            number = grid[row + side[0]][col + side[1]]
            if number in seen_numbers or number % 2 == 0 or 0 >= number >= 10:
                return False
            seen_numbers.add(number)

        # Check the totals across the rows
        for r in range(row - 1, row + 2):
            total = 0
            for c in range(col - 1, col + 2):
                number = grid[r][c]
                total += number

            if total != 15:
                return False

        # Check the total across the columns
        for c in range(col - 1, col + 2):
            total = 0
            for r in range(row - 1, row + 2):
                number = grid[r][c]
                total += number

            if total != 15:
                return False

        return True


sol = Solution()
grid = [[3,2,9,2,7],[6,1,8,4,2],[7,5,3,2,7],[2,9,4,9,6],[4,3,8,2,5]]
for row in grid:
    for col in row:
        print(col, end=' ')
    print()
print(sol.numMagicSquaresInside(grid))
