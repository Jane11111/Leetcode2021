# -*- coding: utf-8 -*-
# @Time    : 2021-06-23 14:16
# @Author  : zxl
# @FileName: 397.py

class Solution:


    def recReplace(self,n,dic):

        if n == 1:
            return 0
        if n in dic:
            return dic[n]
        ans = 0
        if n%2 == 0:
            ans = 1+self.recReplace(n//2,dic)
        else:
            ans = min(1+self.recReplace(n+1,dic),1+self.recReplace(n-1,dic))
        dic[n] = ans
        return ans

    def integerReplacement(self, n: int) -> int:

        dic = {}

        ans = self.recReplace(n,dic)
        return ans



