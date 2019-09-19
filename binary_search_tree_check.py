'''
Given a binary tree, check if it is a binary search tree. 
This solution implements a recursive approach to the problem.
'''

class Node:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val


class TreeFunctionalities():
    def __init__(self, root=None):
        self.root = root

    def preorder(self, root):
        if root:
            self.preorder(root.left)
            print(root.val, end=" ")
            self.preorder(root.right)

    def checkBST(self, root, lower=float('-inf'), upper=float('inf')):
        if root == None:
            return True
        if root.val < lower or root.val > upper:
            return False
        if not self.checkBST(root.left, lower, root.val):
            return False
        if not self.checkBST(root.right, root.val, upper):
            return False
        return True


# Driver code follows to test functionality of checkBST function

# Test Tree 1
root1 = Node(4)
root1.left = Node(2)
root1.right = Node(5)
root1.left.left = Node(1)
root1.left.right = Node(3)

# Test Tree 2
root2 = Node(5)
root2.left = Node(1)
root2.right = Node(6)
root2.right.left = Node(4)
root2.right.right = Node(7)

tree_list = [root1, root2]
tree_func_obj = TreeFunctionalities()

for tree in tree_list:
    print('The preorder traversal is: ')
    tree_func_obj.preorder(tree)

    if tree_func_obj.checkBST(tree):
        print('\nThis is a Binary Search Tree!\n')
    else:
        print('\nThis is NOT a Binary Search Tree!\n')
