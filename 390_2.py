# -*- coding: utf-8 -*-
# @Time    : 2021-06-22 22:20
# @Author  : zxl
# @FileName: 390_2.py



class Solution:

    def recFind(self,n,d,dic):
        if n == 1:
            return n
        if n in dic:
            return dic[n]

        pos = self.recFind(n//2,1-d,dic)

        if d == 0:
            num = pos*2
        else:
            if n%2:
                num = pos*2
            else:
                num = pos*2-1
        dic[n] = num
        return num





    def lastRemaining(self, n: int) -> int:

        dic = {}

        ans = self.recFind(n,0,dic)

        return ans





