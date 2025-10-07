# Last updated: 10/7/2025, 10:28:41 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1] * n for _ in range(m)]
        
        topRow, bottomRow = 0, m - 1
        leftColumn, rightColumn = 0, n - 1
        
        while head:
            # Fill top row
            for col in range(leftColumn, rightColumn + 1):
                if not head:
                    break
                matrix[topRow][col] = head.val
                head = head.next
            topRow += 1
            
            # Fill right column
            for row in range(topRow, bottomRow + 1):
                if not head:
                    break
                matrix[row][rightColumn] = head.val
                head = head.next
            rightColumn -= 1
            
            # Fill bottom row
            for col in range(rightColumn, leftColumn - 1, -1):
                if not head:
                    break
                matrix[bottomRow][col] = head.val
                head = head.next
            bottomRow -= 1
            
            # Fill left column
            for row in range(bottomRow, topRow - 1, -1):
                if not head:
                    break
                matrix[row][leftColumn] = head.val
                head = head.next
            leftColumn += 1

            if not head:
                    break
        return matrix