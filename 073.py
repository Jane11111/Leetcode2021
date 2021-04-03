# -*- coding: utf-8 -*-
# @Time    : 2021-03-21 15:49
# @Author  : zxl
# @FileName: 073.py


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        rows = set([])
        cols = set([])
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        l = len(rows)
        r = len(cols)
        i = 0
        j = 0
        while i<l or j<r:
            if i<l:
                for k in range(i,l):
                    pass
            if j<r:
                pass

            l = len(rows)
            r = len(cols)