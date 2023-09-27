# 1672. Richest Customer Wealth
# https://leetcode.com/problems/richest-customer-wealth/

def maximumWealth(accounts):
    max = float("-inf")
    for person in accounts:
        sum_of_wealth = 0
        for account in person:
            sum_of_wealth += account
        if(sum_of_wealth > max):
            max = sum_of_wealth
    return max


accounts = [[1, 2, 3], [3, 2, 1]]
print(f'Output: {maximumWealth(accounts)}')
accounts = [[1,5],[7,3],[3,5]]
print(f'Output: {maximumWealth(accounts)}')
