# -*- coding: utf-8 -*-
# @Time    : 2021-05-13 15:53
# @Author  : zxl
# @FileName: 070_2.py


class Solution:
    def climbStairs(self, n: int) -> int:


        dp = [1 for i in range(n+1)]
        for i in range(2,n+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n]

obj =Solution()
n = 3
ans = obj.climbStairs(n)
print(ans)