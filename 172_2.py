# -*- coding: utf-8 -*-
# @Time    : 2021-05-30 20:20
# @Author  : zxl
# @FileName: 172_2.py




class Solution:
    def trailingZeroes(self, n: int) -> int:


        count = 0

        for i in range(1,n+1):
            while i%5 == 0:
                i/=5
                count+=1
        return count

