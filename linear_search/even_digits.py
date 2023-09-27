# 1295. Find Numbers with Even Number of Digits
# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
import math


def countDigits(num):
    c = 0
    if num < 0:
        num = abs(num)
    if num == 0:
        return 1
    while (num > 0):
        c += 1
        num = num // 10
    return c


def countDigitsAlternate(num):
    return len(str(num))
    # return math.floor(math.log10(444)+1)


def evenDigits(nums):
    count = 0
    for i in range(len(nums)):
        if countDigits(nums[i]) % 2 == 0:
            count += 1
    return count


nums = [-12, 345, 2, 6, 7896]
print(evenDigits(nums))
nums = [555, 901, 482, 1771]
print(evenDigits(nums))
