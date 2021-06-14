# -*- coding: utf-8 -*-
# @Time    : 2021-06-10 17:43
# @Author  : zxl
# @FileName: 1162.py

class Solution:
    def maxDistance(self, grid ) -> int:


        ans = float('-inf')

        lst = []
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    lst.append([i,j])
        if len(lst) == 0 or len(lst) == m*n:
            return -1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    min_dist = float('inf')
                    for x,y in lst:
                        min_dist = min(min_dist,abs(i-x)+abs(j-y))
                    ans = max(ans,min_dist)
        return ans


