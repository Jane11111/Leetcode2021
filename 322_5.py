# -*- coding: utf-8 -*-
# @Time    : 2021-05-19 09:46
# @Author  : zxl
# @FileName: 322_5.py



class Solution:
    def coinChange(self, coins , amount: int) -> int:

        if amount == 0:
            return 0

        dp = []
        for i in range(amount+1):
            dp.append([100000 for j in range(len(coins))])

        for j in range(len(coins)):
            coin = coins[j]
            for i in range( amount+1):
                if j>0:
                    dp[i][j] = min(dp[i][j],dp[i][j-1])
                if i<coin:
                    continue

                if i == coin:
                    dp[i][j] = 1

                dp[i][j] = min(dp[i][j],dp[i-coin][j]+1)

        return dp[amount][len(coins)-1] if dp[amount][len(coins)-1]!=100000 else -1


obj = Solution()
coins = [1,2,5]
amount = 11
ans = obj.coinChange(coins,amount)
print(ans)


