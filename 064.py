# -*- coding: utf-8 -*-
# @Time    : 2021-03-15 14:15
# @Author  : zxl
# @FileName: 064.py


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        m = len(grid)
        n = len(grid[0])

        arr = []
        for i in range(m):
            arr.append([0 for j in range(n)])
        arr[0][0] = grid[0][0]

        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    continue
                min_val= 1000000
                if i-1>=0 :
                    min_val = min(min_val,arr[i-1][j]+grid[i][j])
                if j-1>=0:
                    min_val = min(min_val,arr[i][j-1]+grid[i][j])
                arr[i][j] = min_val
        return arr[m-1][n-1]
obj = Solution()
grid = [[1,2,3],[4,5,6]]
ans = obj.minPathSum(grid)
print(ans)