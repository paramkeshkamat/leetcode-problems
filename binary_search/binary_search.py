# binary search
import math


def binarySearch(arr, target):
    start = 0
    end = len(arr) - 1

    while start < end:
        # mid = (start + end)/2
        mid = math.ceil(start + (end-start)/2)
        if target < arr[mid]:
            end = mid - 1
        elif target > arr[mid]:
            start = mid + 1
        else:
            return mid
    return -1


arr = [2, 6, 22, 45, 48, 55, 67, 68, 75, 89, 97, 104]  # sorted array
result = binarySearch(arr, 4355)
print("Not Found!" if result == -1 else f'target found at index {result}')
