class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memory = {}

        def search(amt) -> int:
            if amt == 0:
                return 0
            elif amt in memory:
                return memory[amt]

            res = float("inf")
            for coin in coins:
                if amt - coin >= 0:
                    res = min(res, 1 + search(amt-coin))

            memory[amt] = res
            return res

        minCoins = search(amount)
        if minCoins == float("inf"):
            return -1
        return minCoins