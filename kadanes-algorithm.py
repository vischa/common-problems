'''
Given an integer array, find the contiguous subarray
which has the largest sum and return its sum.

The solution explores dynamic programming approach by using Kadane's algorithm.
'''

def maxSubArray(nums):
    new = [0]*len(nums)
    new[0] = nums[0]
    for i in range(1, len(nums)):        
        new[i] = max (nums[i], new[i-1]+nums[i])
        
    return max(new)

#test code
input_array = [-2,1,-3,4,-1,2,1,-5,4]
print("Maximum subarray sum is {}".format(maxSubArray(input_array)))
