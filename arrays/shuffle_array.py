# 1470. Shuffle the Array
# https://leetcode.com/problems/shuffle-the-array/

def shuffle(nums, n):
    result = []
    for i in range(n):
        result.append(nums[i])
        result.append(nums[i+n])
    return result


# [2,3,5,4,1,7]
'''
    n=3
    i=0
    v=2

    n=3
    i=1
    v=5

    n=3
    i=1
    v=2

    n=3
    i=3
    v=3

    n=3
    i=4
    v=4

    n=3
    i=5
    v=7
'''

nums = [2, 5, 1, 3, 4, 7]
print(shuffle(nums, 3))
nums = [1,2,3,4,4,3,2,1]
print(shuffle(nums, 4))
nums = [1,1,2,2]
print(shuffle(nums, 2))
