from typing import List


class Solution:
    """https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
    * constraints:
        - buy idx < sell idx
        - if profit > 0, then right value > left value else profit = 0
    """

    def maxProfitNaive(self, prices: List[int]) -> int:
        """Time Limit Exceeded: O(n^2)"""
        max_profit = 0
        for idx, buy_price in enumerate(prices):
            for sell_price in prices[idx:][::-1]:
                candidate_profit = sell_price - buy_price
                if candidate_profit > max_profit:
                    max_profit = candidate_profit
        return max_profit

    def maxProfit(self, prices: List[int]) -> int:
        """
        we don't know price is increasing or decreasing after or before 1 day
        for buy price:
            - if increase, our profit will decrease
            - if decrease, our profit will increase
        for sell price:
            - if increase, our profit will increase
            - if decrease, our profit will decrease

        sell price가 증가하면 증가한 쪽으로 계산
        buy pricer 감소하면 감소한 쪽으로 계산
        """
        max_profit = 0
        for i, curr_price in enumerate(prices):
            if i == 0:
                buy_price = curr_price
                continue
            sell_price = curr_price
            buy_price = min(buy_price, curr_price)
            max_profit = max(max_profit, sell_price - buy_price)

        return max_profit
