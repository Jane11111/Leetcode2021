# -*- coding: utf-8 -*-
# @Time    : 2021-05-19 14:18
# @Author  : zxl
# @FileName: 807.py



class Solution:
    def maxIncreaseKeepingSkyline(self, grid ) -> int:


        m = len(grid)
        n = len(grid[0])

        arr1 = [0 for i in range(m)]
        arr2 = [0 for i in range(n)]

        for i in range(m):
            for j in range(n):
                arr1[i] = max(arr1[i],grid[i][j])
                arr2[j] = max(arr2[j],grid[i][j])
        ans = 0
        for i in range(m):
            for j in range(n):
                ans+= min(arr1[i],arr2[j])-grid[i][j]
        return ans