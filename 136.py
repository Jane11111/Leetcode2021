# -*- coding: utf-8 -*-
# @Time    : 2021-04-19 10:47
# @Author  : zxl
# @FileName: 136.py



class Solution:
    def singleNumber(self, nums ) :

        a = 0
        for num in nums:
            a = a ^ num
        return a