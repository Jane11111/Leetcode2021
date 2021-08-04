# -*- coding: utf-8 -*-
# @Time    : 2021-07-31 13:44
# @Author  : zxl
# @FileName: Offer010_2.py


class Solution:
    def numWays(self, n: int) -> int:

        if n == 0:
            return 1

        if n == 1:
            return 1
        if n == 2:
            return 2

        n1 = 1
        n2 = 2
        for i in range(3,n+1):
            tmp = n1+n2
            n1 = n2
            n2 = tmp%1000000007
        return n2

obj = Solution()
n = 7
ans = obj.numWays(n)
print(ans)
