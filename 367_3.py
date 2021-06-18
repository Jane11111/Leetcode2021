# -*- coding: utf-8 -*-
# @Time    : 2021-06-18 16:00
# @Author  : zxl
# @FileName: 367_3.py


class Solution:
    def isPerfectSquare(self, num: int) -> bool:


        xk = num

        while xk**2 - num> 1e-3:
            xk = xk- (xk*xk-num)/(2*(xk))

        xk = int(xk)

        return xk**2 == num




obj = Solution()
num = 16
ans = obj.isPerfectSquare(num)
print(ans)



