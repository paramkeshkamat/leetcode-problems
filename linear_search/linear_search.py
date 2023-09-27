# linear search function
def linearSearch(arr, target):
    if len(arr) == 0:
        return -1
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# linear search function for 2D array
def linearSearch2D(arr, target):
    if len(arr) == 0:
        return -1
    for row in range(len(arr)):
        for col in range(len(arr[row])):
            if arr[row][col] == target:
                return [row, col]
    return -1


arr = [3, 4, 5, 33, 22, 11, 38]
result = linearSearch(arr, 5)
print("Not Found!" if result == -1 else f'target found at index {result}')

arr2D = [
    [3, 4, 5],
    [33, 22, 11],
    [38, 23, 67]
]
result2D = linearSearch2D(arr2D, 5)
print("Not Found!" if result2D == -1 else f'target found at {result2D}')
