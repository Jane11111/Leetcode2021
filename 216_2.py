# -*- coding: utf-8 -*-
# @Time    : 2021-07-13 16:33
# @Author  : zxl
# @FileName: 216_2.py



class Solution:

    def recurSolve(self,idx,k,n,sum_val,lst,ans):

        if sum_val == n:
            if len(lst) == k:
                ans.append([item for item in lst])
            return
        if len(lst) == k:
            return

        for i in range(idx,10):
            lst.append(i)
            self.recurSolve(i+1,k,n,sum_val+i,lst,ans)

            lst.pop()





    def combinationSum3(self, k: int, n: int):

        lst = []
        ans = []
        self.recurSolve(1,k,n,0,lst,ans)
        return ans




