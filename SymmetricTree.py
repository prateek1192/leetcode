# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        return self.sym(root, root)
    
    def sym(self, node1, node2):
        if not node1 and not node2:
            return True
        if node1 and not node2:
            return False
        if node2 and not node1:
            return False
        if node1.val != node2.val:
            return False
        return (node1.val == node2.val and self.sym(node1.left, node2.right) and self.sym(node1.right, node2.left))
