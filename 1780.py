# -*- coding: utf-8 -*-
# @Time    : 2021-03-08 20:57
# @Author  : zxl
# @FileName: 1780.py

import math

class Solution(object):

    def recursiveCheck(self,n,k):
        if n<0:
            return False
        if n == 0:
            return True

        m = int(math.log(n,3)) + 1
        for i in range(k,m,1):
            f = self.recursiveCheck(n-3**i,i+1)
            if f:
                return True
        return False

    def checkPowersOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return self.recursiveCheck(n,0)



obj = Solution()
n = 21
f = obj.checkPowersOfThree(n)
print(f)