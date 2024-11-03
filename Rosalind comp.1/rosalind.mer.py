def merge_sort(A, B):
    C = []
    i, j = 0, 0
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1
    C += A[i:]
    C += B[j:]
    return C

n = 4
A = 2, 4, 10, 18
m = 3
B = -5, 11, 12


C = merge_sort(A,B)
for i in C:
        print(i, end=" ")
print()