# -*- coding: utf-8 -*-
# @Time    : 2021-05-15 11:51
# @Author  : zxl
# @FileName: 069_5.py



class Solution:

    def mySqrt(self, x: int) -> int:

        # 没有整数限制
        lo = 0
        hi = x
        while True:

            m = (lo+hi)/2

            if abs(m**2-x)<1e-3:
                return m

            elif m**2< x:
                lo = m
            else:
                hi = m

    # def mySqrt(self, x: int) -> int:
    #
    #     lo = 0
    #     hi = x
    #     while int(lo)!=int(hi):
    #
    #         m = (lo+hi)//2
    #         if (m+1)**2<=x:
    #             lo = m+1
    #         else:
    #             hi = m
    #     return lo