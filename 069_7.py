# -*- coding: utf-8 -*-
# @Time    : 2021-07-14 16:36
# @Author  : zxl
# @FileName: 069_7.py


class Solution:
    def mySqrt(self, x: int) -> int:

        l = 1
        h = x
        while l<h  and int(l)!=int(h):

            m = int((l+h+1)/2) # 偏右的位置

            if m*m<=x:
                l = m

            else:
                h = m-1

        return int(l)
obj = Solution()
x = 8
ans = obj.mySqrt(x)
print(ans)