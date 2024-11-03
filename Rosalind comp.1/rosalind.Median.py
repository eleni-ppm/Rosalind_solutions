
# Given: A positive integer n≤105 and an array A[1..n] of integers from −105 to 105, a positive number k≤n.
#Return: The k-th smallest element of A.

def Median(n, A, k):
    v = n//2
    SL, SV, SR = [], [], []
    for i in range(n):
        if A[i] < A[v]: SL.append(A[i])
        if A[i] == A[v]: SV.append(A[i])
        if A[i] > A[v]: SR.append(A[i])
    if k <= len(SL):
        Median(len(SL), SL, k)
    if len(SL) < k and k <=len(SL)+len(SV):
        print(A[v])
        return A[v]
    if k > len(SL)+len(SV):
        Median(len(SR), SR, k-len(SL)-len(SV))

n = 11
A = 2, 36, 5, 21, 8, 13, 11, 20, 5, 4, 1
k = 8

res = Median(n,A,k)
