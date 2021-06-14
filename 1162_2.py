# -*- coding: utf-8 -*-
# @Time    : 2021-06-10 17:49
# @Author  : zxl
# @FileName: 1162_2.py




class Solution:
    def maxDistance(self, grid ) -> int:

        m = len(grid)
        n = len(grid[0])
        max_val = 100001

        ans = []
        for i in range(m):
            ans.append([max_val for j in range(n)])

        for i in range(m):
            for j in range(n):
                if grid[i][j ] == 1:
                    ans[i][j] = 0
                else:

                    for x,y in [[i-1,j],[i,j-1]]:
                        if x>=0 and x<m and y >=0 and y<n:
                            ans[i][j] = min(ans[i][j],ans[x][y]+1)



        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if grid[i][j ] == 1:
                    ans[i][j] = 0
                else:
                    for x,y in [[i+1,j],[i,j+1]]:
                        if x>=0 and x<m and y >=0 and y<n:
                            ans[i][j] = min(ans[i][j],ans[x][y]+1)
        for i in range(m):
            for j in range(n-1,-1,-1):
                if grid[i][j ] == 1:
                    ans[i][j] = 0
                else:
                    for x,y in [[i+1,j],[i,j-1]]:
                        if x>=0 and x<m and y >=0 and y<n:
                            ans[i][j] = min(ans[i][j],ans[x][y]+1)
        for i in range(m-1,-1,-1):
            for j in range(n):
                if grid[i][j ] == 1:
                    ans[i][j] = 0
                else:
                    for x,y in [[i-1,j],[i,j+1]]:
                        if x>=0 and x<m and y >=0 and y<n:
                            ans[i][j] = min(ans[i][j],ans[x][y]+1)
        val = -1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    continue
                val = max(val,ans[i][j])
        if val >= max_val:
            return -1
        return val

obj = Solution()

grid = [[1,0,1],[0,0,0],[1,0,1]]
ans = obj.maxDistance(grid)
print(ans)