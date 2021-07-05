# -*- coding: utf-8 -*-
# @Time    : 2021-07-05 10:50
# @Author  : zxl
# @FileName: 007_2.py


class Solution:
    def reverse(self, x: int) -> int:
        op = 1
        if x<0:
            op = -1
            x = abs(x)


        ans = 0

        while x:
            num = x%10
            x//=10
            ans = ans*10+num
        if ans > 2**31-1 or ans < -2**31:
            ans = 0
        return ans*op

