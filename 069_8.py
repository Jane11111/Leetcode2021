# -*- coding: utf-8 -*-
# @Time    : 2021-07-14 16:46
# @Author  : zxl
# @FileName: 069_8.py




class Solution:
    def mySqrt(self, x: int) -> int:


        if x == 0:
            return 0


        mk = x

        while abs(mk*mk-x)>1e-5:
            mk = 0.5*mk+(x/(2*mk))
        return int(mk)

obj = Solution()
x = 10
ans = obj.mySqrt(x)
print(ans)