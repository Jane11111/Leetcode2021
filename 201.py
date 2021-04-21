# -*- coding: utf-8 -*-
# @Time    : 2021-04-21 16:11
# @Author  : zxl
# @FileName: 201.py



class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:

        i= 0
        m = left
        n = right
        while m!=n:
            m>>=1
            n>>=1
            i+=1
        return m<<i