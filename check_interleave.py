'''
Check whether a given string is an interleaving of two other given strings.
e.g. ”dabecf” is an interleaved string from ”abc” and ”def”, since it preserves the order along with interleave.
'''

def checkInterleaved(A,B,C):
    for i in range(len(C)):
        if len(A) > 0:
            if C[i]==A[0]:
                list_A = list(A)
                list_A.pop(0)
                A = "".join(list_A)
                continue
        if len(B) > 0:
            if C[i]==B[0]:
                list_B = list(B)
                list_B.pop(0)
                B = "".join(list_B)
                continue
    if (len(A)==0 and len(B)==0):
        return True
    return False
    
#Driver code for testing the solution

A = "AB"
B = "CD"
C = ['ABCD', 'ACBD', 'BACD' , 'ACDB','CABD','CADB','CDAB', 'ABDC']
for item in C:
    if checkInterleaved(A, B, item) == True:
        print(item + " is interleaved of " + A + " and " + B + '\n')
    else:
        print(item + " is not interleaved of " + A + " and " + B + '\n')
