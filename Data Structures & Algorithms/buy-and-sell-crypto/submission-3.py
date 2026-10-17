class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_buy, profit = prices[0], 0

        for index, price in enumerate(prices):
            min_buy = min(min_buy, price) # we want to always keep the min lowest as possible
            if price-min_buy> 0:
                max_profit = max(max_profit, price-min_buy) # check if the current profit is more than the max profit we have seen so far
            # edge cases: profit being negative 

        return max_profit