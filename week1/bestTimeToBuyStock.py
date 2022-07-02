# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

def maxProfit(prices):
    minPrice = prices[0]
    profit = 0

    for i in range(1, len(prices)):
        if prices[i] - minPrice > profit:
            profit = prices[i] - minPrice
        if prices[i] < minPrice:
            minPrice = prices[i]
    
    return profit

print(maxProfit([7,6,4,3,1]))