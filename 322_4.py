# -*- coding: utf-8 -*-
# @Time    : 2021-05-19 09:27
# @Author  : zxl
# @FileName: 322_4.py


class Solution:
    def coinChange(self, coins , amount: int) -> int:

        if amount == 0:
            return 0


        dp = [100000 for i in range(amount+1)]



        for i in range( amount+1):
            for coin in coins:
                if i<coin:
                    continue

                if coin == i:
                    dp[i] = 1
                else:
                    dp[i] = min(dp[i],dp[i-coin]+1)
        return int(dp[amount]) if dp[amount] != 100000 else -1

obj = Solution()
coins = [2,5, 1]
amount = 11
ans = obj.coinChange(coins,amount)
print(ans)