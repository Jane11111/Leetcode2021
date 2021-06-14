# -*- coding: utf-8 -*-
# @Time    : 2021-06-14 20:53
# @Author  : zxl
# @FileName: 518_4.py




class Solution:
    def change(self, amount: int, coins ) -> int:


        dp = [0 for i in range(amount+1)]
        dp[0] = 1

        for coin in coins:

            for i in range(coin,amount+1):
                dp[i] += dp[i-coin]
        return dp[amount]

