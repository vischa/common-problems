"""
Given an n-ary tree, return the preorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:

    def __init__(self):
        self.result=[]
        
    def preorder_recursion(self, root: 'Node') -> List[int]:
        
        if root:
            self.result.append(root.val)
            for child in root.children:
                self.preorder(child)
        return self.result

    def preorder_iteratioon(self, root: 'Node') -> List[int]:
        
        stack=[root]
        while stack:
            item = stack.pop()
            if item:
                self.result.append(item.val)
                stack+=reversed(item.children)
        return self.result
