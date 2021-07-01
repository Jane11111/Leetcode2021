# -*- coding: utf-8 -*-
# @Time    : 2021-07-01 09:47
# @Author  : zxl
# @FileName: 326.py

import math

class Solution:
    def isPowerOfThree(self, n: int) -> bool:

        if n<=0:
            return False

        x = int(math.log(n,3))
        return 3**x == n or(3**(x+1)) == n

n = 243
obj = Solution()
ans = obj.isPowerOfThree(n)
print(ans)


