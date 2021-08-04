# -*- coding: utf-8 -*-
# @Time    : 2021-08-03 19:44
# @Author  : zxl
# @FileName: 077_6.py


class Solution:

    def recFind(self,n,k,idx,lst,ans):

        if len(lst) == k:
            ans.append([item for item in lst])
            return

        for i in range(idx,n+1):
            lst.append(i)

            self.recFind(n,k,i+1,lst,ans)
            lst.pop()


    def combine(self, n: int, k: int) :


        lst = []
        ans = []
        self.recFind(n,k,1,lst,ans)
        return ans