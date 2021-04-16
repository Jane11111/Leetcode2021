# -*- coding: utf-8 -*-
# @Time    : 2021-04-16 17:00
# @Author  : zxl
# @FileName: 059.py

class Solution:




    def generateMatrix(self, n: int) :

        matrix = []
        for i in range(n):
            matrix.append([0 for i in range(n)])

        v = 1
        for i in range(n//2+n%2):
            s = i
            e = n-i-1
            if s==e:
                matrix[s][e] = v
            l = e-s
            next_v = v+4*(e-s)
            for j in range(s,e):
                matrix[i][j] = v
                matrix[j][e] = v+l
                matrix[e][e-(j-i)] = v+2*l
                matrix[e-(j-i)][i] = v+3*l
                v+=1
            v = next_v
        return matrix

obj = Solution()
n = 1
ans = obj.generateMatrix(n)
print(ans)

