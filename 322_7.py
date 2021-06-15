# -*- coding: utf-8 -*-
# @Time    : 2021-06-15 11:22
# @Author  : zxl
# @FileName: 322_7.py



class Solution:
    def coinChange(self, coins , amount: int) -> int:

        if amount == 0:
            return 0


        dp = [float('inf') for i in range(amount+1)]
        dp[0] = 0
        for coin in coins:
            for v in range(coin,amount+1):
                dp[v] = min(dp[v],dp[v-coin]+1)


        if dp[amount] == float('inf'):
            return -1
        return dp[amount]






