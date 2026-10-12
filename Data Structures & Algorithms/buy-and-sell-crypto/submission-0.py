class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0

        for i, price in enumerate(prices):
            max_price = max(prices[i:])
            max_profit = max(max_profit, (max_price - price))

        return max_profit