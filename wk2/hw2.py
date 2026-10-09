# def main():
#     input = [8,2,5,3,9,4,7,6,1]
#     print(quickSort(input, 0, len(input) - 1))


# def quickSort(array : list, start : int, end : int):
#     if end <= start: return # Base Case

#     pivot = partition(array, start, end)
#     quickSort(array, start, pivot - 1)
#     quickSort(array, pivot + 1, end)
#     return array

# def partition(arr, low, high):
#     pivot = arr[high]
#     i = low - 1
#     for j in range(low, high):
#         if arr[j] <= pivot:
#             i += 1
#             arr[i], arr[j] = arr[j], arr[i]
#     arr[i + 1], arr[high] = arr[high], arr[i + 1]
#     return i + 1

# main()
import numpy as np

def rank_smallest(array, start, end, k):
    nums = array.copy()
    pivot = partition(nums, start, end)
    if pivot == k: return nums[pivot]# base case
    if pivot > k:
        rank_smallest(nums, start, pivot - 1, k)
    elif pivot < k:
        rank_smallest(nums, pivot + 1, end, k)
    else:
        return nums[pivot]
    return

def partition(arr, low, high):
    
    # pivot
    pivot = arr[high] 
    
    # Index of smaller element
    i = (low - 1)
    for j in range(low, high):
        
        # If current element is smaller than or
        # equal to pivot
        if (arr[j] <= pivot):
            
            # increment index of smaller element
            i += 1 
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)

def main():
    input = [8,2,5,3,9,4,7,6,1]
    print(rank_smallest(input, 0, len(input)-1, 2))

main()