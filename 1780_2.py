# -*- coding: utf-8 -*-
# @Time    : 2021-03-08 21:08
# @Author  : zxl
# @FileName: 1780_2.py

import math

class Solution(object):

    def recursiveCheck(self,n,dic):
        if n<0:
            return False
        if n == 0:
            return True
        m = int(math.log(n,3)) + 1
        for i in range(0,m,1):
            if i in dic and dic[i] == True:
                continue

            dic[i] = True
            f = self.recursiveCheck(n-3**i,dic)
            if f:
                return True
            dic[i] = False
        return False

    def checkPowersOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return self.recursiveCheck(n,{})

obj = Solution()
res = obj.checkPowersOfThree(21)
print(res)