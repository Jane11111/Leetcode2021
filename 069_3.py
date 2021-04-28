# -*- coding: utf-8 -*-
# @Time    : 2021-04-27 09:38
# @Author  : zxl
# @FileName: 069_3.py


# 二分法
class Solution:
    def mySqrt(self, x: int) -> int:


        i = 0
        j = x
        while int(i)<int(j):

            m = (i+j)/2
            if m*m == x:
                return int(m)
            elif m*m < x:
                i=m
            else:
                j=m



        return int(i)


obj = Solution()
x = 4
ans = obj.mySqrt(x)
print(x)