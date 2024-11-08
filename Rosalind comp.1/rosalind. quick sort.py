#Given: A positive integer n≤105 and an array A[1..n] of integers from −105 to 105.
#Return: A sorted array A[1..n].

#another approach 

from random import randint


def quicksort(a):
    '''Uses the quicksort algorithm to sort an array a.'''
    # Check that the list is trivally sorted.
    if len(a) <= 1:
        return a

    # Choose a pivot location and divide items into sets of less, equal, or greater.
    pivot = randint(0, len(a)-1)
    less, equal, greater = [], [], []
    for x in a:
        if x < a[pivot]:
            less.append(x)
        elif x == a[pivot]:
            equal.append(x)
        else:
            greater.append(x)

    # Quicksort the two unsorted sets.
    return quicksort(less) + equal + quicksort(greater)

n2 = 7
a = 5, -2, 4, 7, 8, -10, 11

b = quicksort(a)
print(b)


