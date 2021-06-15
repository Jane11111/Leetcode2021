# -*- coding: utf-8 -*-
# @Time    : 2021-06-15 11:56
# @Author  : zxl
# @FileName: 070_5.py



class Solution:
    def climbStairs(self, n: int) -> int:

        if n<=2:
            return n


        n1 = 1
        n2 = 2

        for i in range(3,n+1):
            n3 = n1+n2
            n1 = n2
            n2 = n3
        return n3

obj = Solution()
n = 10
ans = obj.climbStairs(n)
print(ans)