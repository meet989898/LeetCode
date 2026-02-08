# Last updated: 2/8/2026, 6:19:44 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isBalanced(self, root: Optional[TreeNode]) -> bool:
9        def dfs(node):
10            if not node:
11                return 0
12            
13            left = dfs(node.left)
14            if left == -1: return -1
15            
16            right = dfs(node.right)
17            if right == -1: return -1
18            
19            if abs(left - right) > 1:
20                return -1
21            
22            return 1 + max(left, right)
23            
24        return dfs(root) != -1