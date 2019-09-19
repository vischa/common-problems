'''
Second array is a shuffled version of the first, with a missing element. Find the missing element.
'''

arr1 = [-2, -2, -3, -6, -1]
arr2 =  [-1, -6, -2, -2]

from collections import Counter
a1 = Counter(arr1)
a2 = Counter(arr2)
for key, value in a1.items():
    if key in a2.keys():
        if a2[key]!=a1[key]:
            print('Missing element is {}'.format(key))
    else:
        print('Missing element is {}'.format(key))
