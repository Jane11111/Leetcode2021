# -*- coding: utf-8 -*-
# @Time    : 2021-05-12 10:49
# @Author  : zxl
# @FileName: Offer029_2.py


class Solution:
    def spiralOrder(self, matrix ) :

        m = len(matrix)
        if m==0:
            return []
        n = len(matrix[0])

        rs = 0
        re = m-1
        cs = 0
        ce = n-1

        lst = []
        while rs<=re and cs<=ce:
            if rs == re:
                for i in range(cs,ce+1):
                    lst.append(matrix[rs][i])
                break
            if cs == ce:
                for i in range(rs,re+1):
                    lst.append(matrix[i][cs])
                break

            for i in range(cs,ce):
                lst.append(matrix[rs][i])
            for i in range(rs,re):
                lst.append(matrix[i][ce])
            for i in range(ce,cs,-1):
                lst.append(matrix[re][i])
            for i in range(re,rs,-1):
                lst.append(matrix[i][cs])
            rs+=1
            re-=1
            cs+=1
            ce-=1
        return lst


