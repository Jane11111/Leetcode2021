# -*- coding: utf-8 -*-
# @Time    : 2021-05-24 22:35
# @Author  : zxl
# @FileName: 096_2.py



class Solution:

    def recsiveFind(self,n,dic):
        if n in dic:
            return dic[n]

        count = 0
        for i in range(1,n+1):
            l = self.recsiveFind(i-1,dic)
            r = self.recsiveFind(n-i,dic)
            count+=l*r
        dic[n] = count
        return count

    def numTrees(self, n: int) -> int:
        dic = {}
        dic[0] = 1
        dic[1] = 1

        ans = self.recsiveFind(n,dic)
        return ans


