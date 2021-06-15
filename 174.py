# -*- coding: utf-8 -*-
# @Time    : 2021-06-15 17:11
# @Author  : zxl
# @FileName: 174.py

class Solution:
    def calculateMinimumHP(self, dungeon) -> int:


        m = len(dungeon)
        n = len(dungeon[0])

        dp = []
        for i in range(m):
            dp.append([0 for j in range(n)])

        dp[m-1][n-1] = 0 if dungeon[m-1][n-1]>0 else abs(dungeon[m-1][n-1])+1

        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if i == m-1 and j== n-1:
                    continue
                min_power = float('inf')
                if i+1<m: # 只需要保证到下面这个格子时，生命大于等于下面这个格子需要的即可
                    tmp = dungeon[i][j]-dp[i+1][j]
                    if tmp<=0:
                        min_power = min(min_power,abs(tmp))
                    else:
                        min_power = min(min_power,0)
                if j+1<n:# 只需要保证到右面这个格子时，生命大于等于右面这个格子需要的即可
                    tmp = dungeon[i][j]-dp[i][j+1]
                    if tmp<=0:
                        min_power = min(min_power,abs(tmp))
                    else:
                        min_power = min(min_power,0)
                if dungeon[i][j]<=0: # 需要保证站在这个格子生命不会降为0
                    min_power = max(min_power,abs(dungeon[i][j])+1)
                dp[i][j] = min_power
        return max(dp[0][0],1)




obj = Solution()
dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
ans = obj.calculateMinimumHP(dungeon)
print(ans)







