# -*- coding: utf-8 -*-
# @Time    : 2021-04-23 11:05
# @Author  : zxl
# @FileName: Offer015_2.py



class Solution:
    def hammingWeight(self, n: int) -> int:

        count = 0

        while n:
            count+=1
            n = n&(n-1)
        return count