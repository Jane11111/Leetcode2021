# -*- coding: utf-8 -*-
# @Time    : 2021-08-03 10:32
# @Author  : zxl
# @FileName: 054_2.py

class Solution:
    def spiralOrder(self, matrix ) :


        m = len(matrix)
        n = len(matrix[0])
        lst = []

        s1 = 0
        e1 = m-1
        s2 = 0
        e2 = n-1

        while s1<=e1 and s2<=e2:


            if s1 == e1:
                for i in range(s2,e2+1):
                    lst.append(matrix[s1][i])
            elif s2 == e2:
                for i in range(s1,e1+1):
                    lst.append(matrix[i][s2])

            else:
                for i in range(s2,e2):
                    lst.append(matrix[s1][i])
                for i in range(s1,e1):
                    lst.append(matrix[i][e2])
                for i in range(e2,s2,-1):
                    lst.append(matrix[e1][i])
                for i in range(e1,s1,-1):
                    lst.append(matrix[i][s2])

            s1+=1
            e1-=1
            s2+=1
            e2-=1
        return lst


