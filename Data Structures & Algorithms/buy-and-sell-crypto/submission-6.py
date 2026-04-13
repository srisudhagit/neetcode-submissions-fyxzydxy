class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = maxprofit = 0
        lowestPrice = prices[0]

        for day,price in enumerate(prices):
            if price < lowestPrice:
                lowestPrice = price
            else:
                profit = price - lowestPrice
                if profit > maxprofit:
                    maxprofit = profit
                
        return maxprofit

