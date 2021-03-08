# -*- coding: utf-8 -*-
# @Time    : 2021-03-06 23:27
# @Author  : zxl
# @FileName: 1137_3.py

class Solution(object):

    def recursiveCal(self,n,dic):

        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        if n in dic:
            return dic[n]

        if n-1 in dic:
            l1 = dic[n-1]
        else:
            l1 = self.recursiveCal(n-1,dic)
            dic[n-1] = l1

        if n-2 in dic:
            l2 = dic[n-2]
        else:
            l2 = self.recursiveCal(n-2,dic)
            dic[n-2] = l2

        if n-3 in dic:
            l3 = dic[n-3]
        else:
            l3 = self.recursiveCal(n-3,dic)
            dic[n-3] = l3

        l = l1 + l2 + l3
        dic[n] = l
        return l


    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """

        return self.recursiveCal(n,{})


obj = Solution()
n = 25
print(obj.tribonacci(n))