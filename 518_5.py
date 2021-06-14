# -*- coding: utf-8 -*-
# @Time    : 2021-06-14 21:11
# @Author  : zxl
# @FileName: 518_5.py




class Solution:
    def change(self, amount: int, coins ) -> int:

        dp = []
        for i in range(amount+1):
            dp.append([0 for j in range(len(coins)+1)])
        coins.insert(0,0)
        dp[0][0] = 1

        for i in range(1,amount+1):
            for j in range(1,len(coins)):
                coin = coins[j]
                if coin>i:
                    continue
                tmp = i-coin
                for k in range(j+1):
                    dp[i][j]+=dp[tmp][k]
        return sum(dp[amount])





