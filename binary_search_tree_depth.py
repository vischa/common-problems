'''
Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Nary-Tree is input.

Solution: Iterate through the stack keeping a counter for depth. 
'''

class Node:

    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    
    def maxDepthIterative(self, root: 'Node') -> int:                
        if not root:
            return 0  
        level=1
        stack = [[root,level]]
        max_level=0
        while stack:
            node =  stack.pop(-1) 
            item = node[0] #node content
            level = node[1] #depth            
            max_level = max(level,max_level)
            level+=1                
            for items in item.children:
                stack.append([items,level])           
        return (max_level)
            
            
            
    def maxDepthRecursive(self, root: 'Node') -> int:
       
        if root is None:
            return 0
        if root.children==[]:
            return 1
        else:
            deptharray = [self.maxDepth(i) for i in root.children]
            return max(deptharray)+1           
