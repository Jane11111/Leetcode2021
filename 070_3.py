# -*- coding: utf-8 -*-
# @Time    : 2021-05-13 15:55
# @Author  : zxl
# @FileName: 070_3.py



class Solution:
    def climbStairs(self, n: int) -> int:


        tmp1 = 1
        tmp2 = 1

        for i in range(2,n+1):
            cur = tmp1+tmp2
            tmp1 = tmp2
            tmp2 = cur
        return tmp2

obj =Solution()
n = 3
ans = obj.climbStairs(n)
print(ans)