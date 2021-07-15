# -*- coding: utf-8 -*-
# @Time    : 2021-07-13 16:16
# @Author  : zxl
# @FileName: 077_4.py


class Solution:

    def recurCombine(self,n,s,k,lst,ans):
        if len(lst) == k:
            ans.append([item for item in lst])
            return

        if len(lst)+(n-s+1)<k:
            return

        for i in range(s,n+1):
            lst.append(i)
            self.recurCombine(n,i+1,k,lst,ans)
            lst.pop()


    def combine(self, n: int, k: int) :

        lst = []
        ans = []
        self.recurCombine(n,1,k,lst,ans)
        return ans