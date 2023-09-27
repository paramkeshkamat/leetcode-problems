# find minimum in a string
def findMinimum(arr):
    minimum = arr[0]
    for i in range(1, len(arr)):
        if (arr[i] < minimum):
            minimum = arr[i]
    return minimum


arr = [4, 33, 44, 56, 2, 33, 24]
print(findMinimum(arr))