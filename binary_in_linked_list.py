'''
Question Source: LeetCode (leetcode.com)

Convert Binary Number in a Linked List to Integer.

Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.
'''

# Definition for singly-linked list.
class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    
    def getDecimalValue(self, head: ListNode) -> int:                      
        values,output=[],0
        while head:
            values.append(head.val)
            head = head.next       
        
        for index,value in enumerate(values[::-1]):        
            output+= value * (2**index)
        return output
