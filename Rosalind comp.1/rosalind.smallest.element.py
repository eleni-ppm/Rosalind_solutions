# Given: A positive integer n≤105 and an array A[1..n] of integers from −105 to 105 a positive integer k≤1000

def heapify(arr, n, i): 
    smallest = i
    l = 2 * i + 1  # left child
    r = 2 * i + 2  # right child

    if l < n and arr[l] < arr[smallest]: 
        smallest = l
    if r < n and arr[r] < arr[smallest]: 
        smallest = r

    if smallest != i: 
        arr[i], arr[smallest] = arr[smallest], arr[i]  # Fix the swap assignment
        heapify(arr, n, smallest)

def buildHeap(arr, n):
    # Build a min heap
    for i in range(n // 2 - 1, -1, -1): 
        heapify(arr, n, i)

def k_smallest_elements(arr, k):
    n = len(arr)
    buildHeap(arr, n)

    result = []
    for _ in range(k):
        # The smallest element is at the root of the heap
        result.append(arr[0])
        # Move the last element to the root and reduce the size of the heap
        arr[0] = arr[-1]
        arr.pop()  # Remove the last element
        n -= 1
        heapify(arr, n, 0)  # Re-heapify the reduced heap

    return result

# Sample input
arr = [4, -6, 7, 8, -9, 100, 12, 13, 56, 17]
k = 3

# Get the k smallest elements
smallest_elements = k_smallest_elements(arr, k)

# Print the result
print(k,smallest_elements)
