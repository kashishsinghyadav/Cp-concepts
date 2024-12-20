# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(root1,root2,lvl):
            if not root1 or not root2:
                return
            if lvl % 2 == 0:
                root1.val, root2.val = root2.val, root1.val
            dfs(root1.left, root2.right, lvl + 1)
            dfs(root1.right, root2.left, lvl + 1)

        dfs(root.left,root.right,0)
        return root
