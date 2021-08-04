# -*- coding: utf-8 -*-
# @Time    : 2021-08-03 12:55
# @Author  : zxl
# @FileName: 059_2.py


class Solution:
    def generateMatrix(self, n: int) :


        if n == 1:
            return [[1]]

        matrix = []
        for i in range(n):
            matrix.append([0 for j in range(n)])

        num = 1

        s = 0
        e = n-1
        while s<=e:

            if s == e:
                matrix[s][e] = num
                break

            for i in range(s,e):
                matrix[s][i] = num
                num+=1
            for i in range(s,e):
                matrix[i][e] = num
                num+=1

            for i in range(e,s,-1):
                matrix[e][i] = num
                num+=1
            for i in range(e,s,-1):
                matrix[i][s] = num
                num+=1
            s+=1
            e-=1
        return matrix


