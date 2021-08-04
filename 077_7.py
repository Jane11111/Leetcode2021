# -*- coding: utf-8 -*-
# @Time    : 2021-08-03 19:49
# @Author  : zxl
# @FileName: 077_7.py


class Solution:

    def recFind(self,n,k,idx,lst,ans):



        if len(lst) == k:
            ans.append([item for item in lst])
            return
        if idx > n:
            return
        self.recFind(n,k,idx+1,lst,ans) #不使用当前的number
        lst.append(idx)
        self.recFind(n,k,idx+1,lst,ans) # 使用当前的number
        lst.pop()


    def combine(self, n: int, k: int) :


        lst = []
        ans = []
        self.recFind(n,k,1,lst,ans)
        return ans


