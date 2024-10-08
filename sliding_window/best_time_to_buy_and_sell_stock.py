from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        - O(n)
        - have n-1 options to buy
        """
        if len(prices) == 1:
            return 0

        min_so_far = prices[0]
        max_prof = -1
        for i, price in enumerate(prices):
            if i == 0:
                continue
            min_so_far = min(min_so_far, price)
            max_prof = max(max_prof, price - min_so_far)

        return max_prof

        