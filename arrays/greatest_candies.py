# 1431. Kids With the Greatest Number of Candies
# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

def kidsWithCandies(candies, extraCandies):
    result = []
    maxCandies = max(candies)
    for i in candies:
        result.append(i+extraCandies >= maxCandies)
    return result


candies = [2, 3, 5, 1, 3]
kidsWithCandies(candies, 3)
