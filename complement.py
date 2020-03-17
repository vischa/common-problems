'''
Given a positive integer, output its complement number. 
The complement strategy is to flip the bits of its binary representation.
'''
class Solution:
    def findComplement(self, num: int) -> int:
        length = len(bin(num))-2
        ones = 2**length - 1
        outout = num ^ ones
        return output
