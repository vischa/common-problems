'''
Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
A leaf is a node with no children.
Definition for a binary tree node:
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
'''

class Solution:
    def maxDepth(self, root):
        leftdepth,rightdepth=0,0
        if not root:
            return 0
        if root:
            leftdepth = self.maxDepth(root.left)
            rightdepth = self.maxDepth(root.right)          
            return max(1+leftdepth,1+rightdepth)
    
