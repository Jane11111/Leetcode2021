# -*- coding: utf-8 -*-
# @Time    : 2021-04-18 12:46
# @Author  : zxl
# @FileName: 069.py


class Solution:
    def mySqrt(self, x: int) -> int:

        x1 = x
        while x1*x1>x :
            x1 = int(0.5*(x1+x/x1))
        return x1


x = 5
obj = Solution()
ans = obj.mySqrt(x)
print(ans)

