# -*- coding: utf-8 -*-
# @Time    : 2021-06-15 20:50
# @Author  : zxl
# @FileName: 304.py




class NumMatrix:

    def __init__(self, matrix ):

        m = len(matrix)
        n = len(matrix[0])
        dp = []
        for i in range(m+1):
            dp.append([0 for j in range(n+1)])
        for i in range(1,m+1):
            for j in range(1,n+1):
                dp[i][j] = dp[i-1][j]+dp[i][j-1]+matrix[i-1][j-1]-dp[i-1][j-1]
        self.dp = dp


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:


        row1+=1
        col1+=1
        row2+=1
        col2+=1

        area = self.dp[row2][col2]-self.dp[row1-1][col2]-self.dp[row2][col1-1]+self.dp[row1-1][col1-1]
        return area



