class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0 
        min_buy = float('inf')
        for price in prices:
            if price < min_buy:
                min_buy = price

            diff = price - min_buy
            max_profit = max(max_profit, diff)
        return max_profit
            

            

        