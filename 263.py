# -*- coding: utf-8 -*-
# @Time    : 2021-04-14 21:20
# @Author  : zxl
# @FileName: 263.py


class Solution:
    def isUgly(self, n: int) -> bool:

        while n%2==0:
            n/=2

        while n%3 == 0:
            n/=3

        while n%5 == 0:
            n/=5

        return n==1

obj = Solution()
n = 14
ans = obj.isUgly(n)
print(ans)