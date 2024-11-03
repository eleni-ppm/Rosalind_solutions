def partition(array):
    new_array, left_array, right_array = [], [], []   #i dont know about this
    new_array.append(array[0])
    for i in range(1, len(array)):
        if array[i] <= array[0]:
            left_array.append(array[i])
        else:
            right_array.append(array[i])
    new_array = left_array + new_array + right_array
    return new_array


n = 9
A = 7, 2, 5, 6, 1, 3, 9, 4, 8
B = partition(A)
for i in B:
    print(i, end=" ")
    print()

# another approach

def two_way_partition(a):
    '''Performs a 2-way partition on the array a.'''
    # Trivial with list comprehensions.
    return [x for x in a[1:] if x <= a[0]] + [a[0]] + [x for x in a[1:] if x > a[0]]

# this works better 
n2= 9
a = 7, 2, 5, 6, 1, 3, 9, 4, 8
a = map(str, two_way_partition(a))
print(a)