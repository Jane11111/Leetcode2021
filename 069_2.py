# -*- coding: utf-8 -*-
# @Time    : 2021-04-19 10:09
# @Author  : zxl
# @FileName: 069_2.py


class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = x
        while low<high and int(low) != int(high):
            m = (low+high)/2
            if m*m<x:
                low = m
            elif m*m>x:
                high = m
            else:
                return m
        return int(low)

obj = Solution()
x = 5
ans = obj.mySqrt(x)
print(ans)

