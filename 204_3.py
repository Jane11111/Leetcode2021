# -*- coding: utf-8 -*-
# @Time    : 2021-07-26 15:35
# @Author  : zxl
# @FileName: 204_3.py



class Solution:
    def countPrimes(self, n: int) -> int:

        if n<=2:
            return 0


        dp = [True for i in range(0,n )]

        ans = 0
        for i in range(2,n ):
            if dp[i]:
                ans+=1
                for j in range(i,(n)//i +1):
                    if i*j< n:
                        dp[i*j] = False
        return ans