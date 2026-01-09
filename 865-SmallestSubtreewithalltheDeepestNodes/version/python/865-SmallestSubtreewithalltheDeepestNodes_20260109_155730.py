# Last updated: 1/9/2026, 3:57:30 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
9        Result = collections.namedtuple("Result", ("node", "dist"))
10        def dfs(node):
11            # Return the result of the subtree at this node.
12            if not node: return Result(None, 0)
13            L, R = dfs(node.left), dfs(node.right)
14            if L.dist > R.dist: return Result(L.node, L.dist + 1)
15            if L.dist < R.dist: return Result(R.node, R.dist + 1)
16            return Result(node, L.dist + 1)
17
18        return dfs(root).node