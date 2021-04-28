# -*- coding: utf-8 -*-
# @Time    : 2021-04-27 09:48
# @Author  : zxl
# @FileName: 069_4.py


class Solution:
    def mySqrt(self, x: int) -> int:


        xk = 1

        while abs(xk*xk-x)>10e-6:
            xk = xk/2+x/(2*xk)


        if (int(xk)+1)**2<=x:
            return int(xk)+1
        else:
            return int(xk)


obj = Solution()
x = 9
ans = obj.mySqrt(x)
print(ans)

