# -*- coding: utf-8 -*-
# @Time    : 2021-03-15 14:09
# @Author  : zxl
# @FileName: 063.py


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        arr = []
        for i in range(m):
            arr.append([0 for j in range(n)])
        if obstacleGrid[m-1][n-1] == 1:
            return 0

        arr[0][0] = 1

        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    continue

                num = 0
                if i-1>=0 and obstacleGrid[i-1][j] == 0:
                    num += arr[i-1][j]
                if j-1 >= 0 and obstacleGrid[i][j-1] == 0:
                    num += arr[i][j-1]
                arr[i][j] = num
        return arr[m-1][n-1]

obj = Solution()
obstacleGrid = [[0,0],[0,1]]
ans = obj.uniquePathsWithObstacles(obstacleGrid)
print(ans)