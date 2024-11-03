# Given: A positive integer n≤105 and an array A[1..n] of integers from −105to 105
#Return: A sorted array A


def heapify(arr, n, i): 
    largest = i
    l = 2 * i + 1  # left child
    r = 2 * i + 2  # right child

    if l < n and arr[l] > arr[largest]: 
        largest = l
    if r < n and arr[r] > arr[largest]: 
        largest = r

    if largest != i: 
        arr[i], arr[largest] = arr[largest], arr[i]  # Fixed the assignment operator
        heapify(arr, n, largest) 
  
def buildHeap(arr, n):
    # Build a maxheap
    for i in range(n//2 - 1, -1, -1): 
        heapify(arr, n, i)

def heapSort(arr):
    n = len(arr)
    buildHeap(arr, n)

    # One by one extract elements from heap
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Swap
        heapify(arr, i, 0)

# Sample input
arr = [2, 6, 7, 1, 3, 5, 4, 8, 9]
heapSort(arr)

# Print sorted array
for i in range(len(arr)): 
    print(arr[i], end=" ")

print()


