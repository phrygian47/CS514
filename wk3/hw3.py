def dHeapSort(arr, d=2):
    
    maxHeapify(arr, i, heap_size, d)


def maxHeapify(arr, i, heap_size, d):
    
    largest = i
    for k in range(1, d + 1):              # check each of the d children
        c = d * i + k                      # k-th child of i
        if c < heap_size and arr[c] > arr[largest]:
            largest = c
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]   # move the smaller value down
        maxHeapify(arr, largest, heap_size, d)         # continue from the child