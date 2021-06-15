# -*- coding: utf-8 -*-
# @Time    : 2021-06-15 11:31
# @Author  : zxl
# @FileName: 518_7.py


class Solution:
    def change(self, amount: int, coins ) -> int:


        dp = [0 for i in range(amount+1)]
        dp[0] = 1

        for coin in coins:
            for v in range(coin,amount+1):
                dp[v] += dp[v-coin]
        return dp[amount]

