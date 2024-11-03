A = 6, 10, 4, 5, 1, 2
def ins(A):
    swap = 0
    for i in range(len(A)):
        k = i
        while k > 0 and A[k] < A[k-1]:
            A[k-1], A[k] = A[k], A[k-1]
            swap += 1
            k -= 1
            return swap


n = 6
A = 6, 10, 4, 5, 1, 2

s = [int(i) for i in A]
print(ins(s))

swap = str(ins(A))
print(swap)
