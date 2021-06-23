# -*- coding: utf-8 -*-
# @Time    : 2021-06-22 15:06
# @Author  : zxl
# @FileName: 371.py



class Solution:
    def getSum(self, a: int, b: int) -> int:

        mask = 0x100000000

        int_max = 0x7FFFFFFF
        int_min = int_max+1


        while b!=0:
            carry = (a&b)<<1
            a = (a^b)%mask
            b = carry%mask

        return a if a<=int_max else ~((a%int_min)^int_max)



