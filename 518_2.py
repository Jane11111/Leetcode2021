# -*- coding: utf-8 -*-
# @Time    : 2021-05-18 21:37
# @Author  : zxl
# @FileName: 518_2.py



class Solution:

    def change(self, amount: int, coins) -> int:


        dp = [0 for i in range(amount+1)]
        dp[0] = 1
        for coin in coins:
            for i in range(coin,amount+1):
                dp[i] += dp[i-coin]
        return dp[amount]


