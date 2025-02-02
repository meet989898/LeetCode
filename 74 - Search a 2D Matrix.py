from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        left, right = 0, len(matrix) - 1
        while left <= right:

            mid = (left + right) // 2

            if matrix[mid][0] <= target and matrix[mid][-1] >= target:

                rowLeft, rowRight = 0, len(matrix[0]) - 1

                while rowLeft <= rowRight:

                    rowMid = (rowLeft + rowRight) // 2

                    if matrix[mid][rowMid] == target:
                        return True

                    elif matrix[mid][rowMid] > target:
                        rowRight = rowMid - 1

                    else:
                        rowLeft = rowMid + 1

                return False

            elif matrix[mid][0] > target:
                right = mid - 1

            else:
                left = mid + 1

        return False




sol = Solution()
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(sol.searchMatrix(matrix, target))