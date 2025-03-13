# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p == root:
            return p
        elif q == root:
            return q

        parents = dict()
        
        def preorder(root, parents):
            if root.left:
                parents[root.left] = root
                preorder(root.left, parents)
            
            if root.right:
                parents[root.right] = root
                preorder(root.right, parents)
        
        preorder(root,parents)
        pp = p
        visited = {p}
        parents[root] = None
        

        while pp != root:
            pp = parents[pp]
            visited.add(pp)

        qq = q
        while qq not in visited:
            qq = parents[qq]
        
        
        return qq
        # time complexity: O(n), space complexity: O(n)



#optimal

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        #optimal top down
        def lca(root):
            if not root:
                return None
            if root == p or root == q:
                return root

            l = lca(root.left)
            r = lca(root.right)

            if l and r:
                return root
            else:
                return l or r
            
        return lca(root)

        # time complexity: O(n), space complexity: O(n)


