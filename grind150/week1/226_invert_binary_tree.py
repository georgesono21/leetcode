# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #intuition we do a top down preorder traversal as we don't need to know anything fron the left and right branches, we just switch the branches and go down the tree

        #O(V + E)
        def preorder(root):
            if root:
                root.left, root.right = root.right, root.left
                preorder(root.left)
                preorder(root.right)
        preorder(root)
        return root
