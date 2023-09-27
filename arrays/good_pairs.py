# 1512. Number of Good Pairs
# https://leetcode.com/problems/number-of-good-pairs/

def numIdenticalPairs(nums):
    result = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if i < j and nums[i] == nums[j]:
                result += 1
    return result


nums = [1, 2, 3, 1, 1, 3]
print(numIdenticalPairs(nums))
nums = [1,1,1,1]
print(numIdenticalPairs(nums))
nums = [1,2,3]
print(numIdenticalPairs(nums))
