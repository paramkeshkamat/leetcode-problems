# find character in a string
def search(str, target):
    for i in range(len(str)):
        if str[i] == target:
            return i
    return -1


result = search("hello", "s")
print("Not Found!" if result == -1 else f'target found at index {result}')
