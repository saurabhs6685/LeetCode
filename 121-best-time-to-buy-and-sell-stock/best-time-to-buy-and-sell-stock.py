from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy = prices[0]
        max_p = 0
        
        for p in prices:
            if p < min_buy:
                min_buy = p
            elif p - min_buy > max_p:
                max_p = p - min_buy
                
        return max_p