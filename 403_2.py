# -*- coding: utf-8 -*-
# @Time    : 2021-05-25 10:51
# @Author  : zxl
# @FileName: 403_2.py



class Solution:

    def canCross(self, stones ) -> bool:

        dp = []
        dic = {}
        for i in range(len(stones)):
            dp.append([False for j in range(len(stones))])
            dic[stones[i]] = i

        if 1 in dic:
            dp[dic[1]][0] = True

        for i in range(1,len(stones)):

            stone = stones[i]

            for j in range(0,i):
                if dp[i][j] == True: #能从stones[j]跳跃到stones[i]

                    k = stones[i]-stones[j]
                    if k-1 >0 and stone+k-1 in dic:
                        dp[dic[stone+k-1]][i] = True
                    if stone+k in dic:
                        dp[dic[stone+k]][i] = True
                    if stone+k+1 in dic:
                        dp[dic[stone+k+1]][i] = True
        for i in range(len(stones)):
            if dp[len(stones)-1][i] == True:
                return True
        return False


