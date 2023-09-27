def reverseArray(arr):
    start = 0
    end = len(arr)-1
    while start <= end:
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start = start + 1
        end = end - 1


arr = [44, 56, 22, 5, 256]
print(arr)

reverseArray(arr)

# in-built reverse function
# arr.reverse()
print(arr)
