# -*- coding: utf-8 -*-
# @Time    : 2021-05-16 15:28
# @Author  : zxl
# @FileName: 062_3.py



class Solution:
    def uniquePaths(self, m: int, n: int) -> int:


        if m==1 or n==1:
            return 1
        if m>n:
            m,n = n,m
        ans = 1

        for i in range(m-1):
            ans*=(m+n-2-i)
        for i in range(1,m):
            ans/=i
        return int(ans)
