class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bestProfit = 0
        lowestPrice = prices[0]

        for price in prices:
            bestProfit = max(bestProfit, price - lowestPrice)
            lowestPrice = min(lowestPrice, price)

        return bestProfit
        