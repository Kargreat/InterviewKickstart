from typing import List

ip_ = [7,3,1,10,5,11,9,18]


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = [0]
        cur_profit = 0
        if len(prices) > 0:
            buy_price = prices[0]

            for i in range(1, len(prices)):
                if prices[i-1] > prices[i]:
                    buy_price = prices[i]
                    profit.append(cur_profit)
                    cur_profit = 0
                else:
                    print(cur_profit, prices[i] - buy_price)
                    cur_profit = max(cur_profit, prices[i] - buy_price)
        profit.append(cur_profit)
        profit = sorted(profit, reverse=True)
        print(profit)
        return sum(profit[:2])


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxProfit(ip_))