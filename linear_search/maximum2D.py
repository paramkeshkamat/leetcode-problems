# function to find maximum in 2D array
def findMaximum(arr):
    max = float("-inf")
    for row in range(len(arr)):
        for col in range(len(arr[row])):
            if arr[row][col] > max: 
                max = arr[row][col]
    return max;

arr = [
    [3, 4, 5],
    [33, 22, 11],
    [38, 23, 67]
]
print(findMaximum(arr))