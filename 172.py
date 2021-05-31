# -*- coding: utf-8 -*-
# @Time    : 2021-05-30 17:39
# @Author  : zxl
# @FileName: 172.py



class Solution:
    def trailingZeroes(self, n: int) -> int:


        v = 1
        count = 0
        for i in range(1,n+1,1):
            v*=i
            while v%10 == 0:
                count+=1
                v/=10
        return count