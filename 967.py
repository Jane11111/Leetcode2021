# -*- coding: utf-8 -*-
# @Time    : 2021-03-06 22:40
# @Author  : zxl
# @FileName: 967.py

import copy
class Solution(object):

    def recursiveFind(self,n,k,nums ):

        res = []
        if n == 0:
            return nums
        for num in nums:

            if num[-1] + k < 10:
                tmp = copy.copy(num)
                tmp.append(num[-1]+k)
                res.append(tmp)
            if num[-1] - k >= 0:
                tmp = copy.copy(num)
                tmp.append(num[-1]-k)
                res.append(tmp)
        return self.recursiveFind(n-1,k,res)
    def lst2num(self,lst):
        res = 0
        base = 1
        for i in range(len(lst)-1,-1,-1):
            res += base * lst[i]
            base *= 10
        return res

    def numsSameConsecDiff(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        if n == 0:
            return []
        nums = []
        for i in range(1,10,1):
            nums.append([i])
        lst = self.recursiveFind(n-1,k,nums)

        res = []
        for item in lst:
            if len(item) == n:
                res.append(self.lst2num(item))
        return list(set(res))

obj = Solution()
n = 3
k = 7
res = obj.numsSameConsecDiff(n,k)
print(res)


