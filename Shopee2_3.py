# -*- coding: utf-8 -*-
# @Time    : 2021-07-05 16:29
# @Author  : zxl
# @FileName: Shopee2_3.py



class Solution:

    def minimumInitHealth(self, rooms, startPoint, endPoint):

        m = len(rooms)
        n = len(rooms[0])

        dp = []
        for i in range(m+1):
            dp.append([float('inf') for j in range(n+1)])

        x, y = endPoint
        if rooms[x][y]<=0:
            h = abs(rooms[x][y])+1

        else:
            h = 1

        dp[x][y] = h

        for i in range(x,-1,-1):
            for j in range(y,-1,-1):

                if i == x and j == y:
                    continue
                p = min(dp[i+1][j],dp[i][j+1])
                if rooms[i][j] <=0:
                    dp[i][j] = p+abs(rooms[i][j])
                else:
                    if rooms[i][j]<p:
                        dp[i][j] = abs(rooms[i][j]-p)
                    else:
                        dp[i][j] = 1
        return dp[startPoint[0]][startPoint[1]]

obj = Solution()
rooms = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
startPoint = [0,0]
endPoint = [2,2]
ans = obj.minimumInitHealth(rooms,startPoint,endPoint)
print(ans)