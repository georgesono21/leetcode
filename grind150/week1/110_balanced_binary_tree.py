# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        intuition: post order traversal, get the height of left and right subtrees, and check if
        the difference between them is within 1, if not, then return False and the larger depth
        of left and right subtrees. For base case, if we reach a node that is null, just return
        True and depth, as a null node is technically still a hieght balanced binary tree


        """

        def postOrder(root, depth):
            if not root:
                return True, depth

            left = postOrder(root.left, depth + 1) if root.left else (True, depth)
            right = postOrder(root.right, depth + 1) if root.right else (True, depth)

            if (abs(left[1] - right[1]) <= 1) and (left[0] and right[0]):
                return True, max(left[1], right[1])
            else:
                return False, max(left[1], right[1])

        return postOrder(root, 0)[0]

        # time O(n) where n is the number of nodes
