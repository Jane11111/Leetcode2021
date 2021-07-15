# -*- coding: utf-8 -*-
# @Time    : 2021-07-14 16:00
# @Author  : zxl
# @FileName: 062_5.py

import numpy as np

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        val = 1
        for i in range(m-1):
            val*=(n+i)
            # if m-i>0:
            val/=(i+1)

        return int(val)

obj = Solution()
m = 53
n = 4
ans = obj.uniquePaths(m,n)
print(ans)

