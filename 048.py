# -*- coding: utf-8 -*-
# @Time    : 2021-04-16 15:39
# @Author  : zxl
# @FileName: 048.py


class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)
        for i in range(n//2):
            s = i
            e = n-s-1
            for j in range(s,e):

                matrix[j][e], matrix[e][e - (j - i)], matrix[e - (j - i)][i],matrix[i][j] = \
                matrix[i][j],matrix[j][e],matrix[e][e-(j-i)],matrix[e-(j-i)][i]

obj = Solution()
matrix = [[1,2],[3,4]]
ans = obj.rotate(matrix)
print(matrix)

