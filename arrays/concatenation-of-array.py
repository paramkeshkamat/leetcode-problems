# 1929. Concatenation of Array
# https://leetcode.com/problems/concatenation-of-array/

def getConcatenation(nums):
    ans = []
    for i in range(len(nums)):
        ans.append(nums[i])
    return ans + nums


nums = [1, 2, 1]
print(getConcatenation(nums))
nums = [1, 3, 2, 1]
print(getConcatenation(nums))
