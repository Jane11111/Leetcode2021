# -*- coding: utf-8 -*-
# @Time    : 2021-05-19 10:52
# @Author  : zxl
# @FileName: 070_4.py



class Solution:
    def climbStairs(self, n: int) -> int:

        amount = n
        coins = [1,2]

        if amount == 0:
            return 1

        dp = []
        for i in range(amount+1):
            dp.append([0 for j in range(len(coins))])



        for i in range(amount + 1):
            for j in range(len(coins)):

                coin = coins[j]

                if i< coin:
                    continue
                if coin == i:
                    dp[i][j] += 1
                # 这个下标j表示这个组合问题，仅考虑到了到j为止的硬币组合
                # 如果是排列问题，需要遍历dp[i-coin]这一行所有的值再加和，并且代码26，27行不能要了
                # dp[i][j] = dp[i][j]+dp[i-coin][j]
                for k in range(len(coins)):
                    dp[i][j] += dp[i-coin][k]

        return sum(dp[amount])


obj =Solution()
n = 3
ans = obj.climbStairs(n)
print(ans)