# -*- coding: utf-8 -*-
# @Time    : 2021-05-26 16:06
# @Author  : zxl
# @FileName: 1420.py


import numpy as np
class Solution:




    def numOfArrays(self, n: int, m: int, k: int) -> int:

        if k==0 or k>m or k>n:
            return 0

        mod = 1000000007

        dp = np.zeros((n+1,k+1,m+1))
        for j in range(1,m+1):
            dp[1][1][j] = 1

        for i in range(2,n+1): # 长度
            for s in range(1,k+1,1): # 代价
                for j in range(1,m+1,1):
                    # if i == 8:
                    #     print(' i am here')
                    v = dp[i-1][s][j]*j
                    for j2 in range(1,j):
                        v+=dp[i-1][s-1][j2]
                    dp[i][s][j] = v%mod
        ans = 0

        for j in range(1,m+1):
            ans += dp[n][k][j]
            ans %= mod
        return int(ans)




obj = Solution()
n = 50
m = 100
k = 25
ans = obj.numOfArrays(n,m,k)
print(ans)







