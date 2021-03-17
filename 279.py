# -*- coding: utf-8 -*-
# @Time    : 2021-03-16 22:50
# @Author  : zxl
# @FileName: 279.py


class Solution(object):



    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        import numpy as np
        while n%4==0:
            n//=4

        if n%8==7:
            return 4
        if n == int(np.sqrt(n))**2:
            return 1
        for i in range(1,n):
            if i*i >n:
                break
            if n-i*i == int(np.sqrt(n-i*i))**2:
                return 2
        return 3
obj = Solution()
n = 12
ans = obj.numSquares(n)
print(ans)
