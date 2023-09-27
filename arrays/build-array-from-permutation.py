# 1920. Build Array from Permutation
# https://leetcode.com/problems/build-array-from-permutation/

def buildArray(nums):
    result = []
    for i in range(len(nums)):
        result.append(nums[nums[i]])
    return result


nums = [0, 2, 1, 5, 3, 4]
print(buildArray(nums))
