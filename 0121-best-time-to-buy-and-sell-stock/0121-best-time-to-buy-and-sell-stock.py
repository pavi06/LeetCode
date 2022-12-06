class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low=10**4
        max_profit=0
        for i,val in enumerate(prices):
            p=val-low
            if val < low:
                low=val
            if p > max_profit:
                max_profit=p
        return max_profit
                
        
        