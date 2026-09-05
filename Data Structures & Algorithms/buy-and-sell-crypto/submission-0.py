class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum_price = prices[0]
        max_profit = 0
        
        for i in range(len(prices)):
            if prices[i] < minimum_price:
                minimum_price = prices[i]
            
            profit = prices[i] - minimum_price
            if max_profit < profit:
                max_profit = profit
        
        return max_profit