# -*- coding: utf-8 -*-
# @Time    : 2021-05-30 20:42
# @Author  : zxl
# @FileName: 172_3.py



class Solution:
    def trailingZeroes(self, n: int) -> int:


        count = 0
        while n:
            n//=5
            count += n
        return count

