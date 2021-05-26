# -*- coding: utf-8 -*-
# @Time    : 2021-05-19 10:12
# @Author  : zxl
# @FileName: 518_3.py



class Solution:

    def change(self, amount: int, coins) -> int:

        if amount == 0:
            return 1


        dp = []
        for i in range(amount+1):
            dp.append([0 for j in range(len(coins))])

        for i in range(amount + 1):
            for j in range(len(coins)):
                coin = coins[j]
                # if i == 2 and j == 0:
                #     print('i am here')

                if j>0:
                    dp[i][j] = max(dp[i][j-1],dp[i][j])

                if i< coin:
                    continue
                if coin == i:
                    dp[i][j] += 1
                # 这个下标j表示这个组合问题，仅考虑到了到j为止的硬币组合
                # 如果是排列问题，需要遍历dp[i-coin]这一行所有的值再加和，并且代码26，27行不能要了
                # 最后返回的是最后一行的sum
                dp[i][j] = dp[i][j]+dp[i-coin][j]
        return dp[amount][len(coins)-1]


obj = Solution()
coins = [2,5,1]
amount = 5
ans = obj.change(amount,coins)
print(ans)