# 1480. Running Sum of 1d Array
# https://leetcode.com/problems/running-sum-of-1d-array/

def runningSum(nums):
    running_sum = []
    sum = 0
    for item in nums:
        sum += item
        running_sum.append(sum)
    return running_sum


'''
sum = 0 
index = 0
item = 1


sum = 1
index = 1
item = 2
'''


nums = [1, 2, 3, 4]
print(runningSum(nums))
nums = [1, 1, 1, 1, 1]
print(runningSum(nums))
nums = [3, 1, 2, 10, 1]
print(runningSum(nums))
