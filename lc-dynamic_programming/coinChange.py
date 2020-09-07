from typing import List
coins = [6,5]
amount = 9


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        min_val = amount + 1
        coins = sorted(coins, reverse=True)
        changes = dict()
        if len(coins) == 0:
            return -1
        if amount == 0:
            return 0
        changes[0] = 0
        local_count_count = list()
        for i in range(1, amount+1):
            min_val = amount + 1
            for coin in coins:
                if coin <= i:
                    if changes[i - coin] != -1:
                        min_val = min(changes[i - coin] + 1, min_val)
            # print(min_val)
            if min_val != amount + 1:
                changes[i] = min_val
            else:
                changes[i] = -1


        return list(changes.values())[-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.coinChange(coins=coins, amount=amount))
