# -*- coding: utf-8 -*-
# @Time    : 2021-07-12 16:25
# @Author  : zxl
# @FileName: 040_3.py




class Solution:



    def recurSolve(self,candidates,idx,sum_val,target,lst,ans):


        if sum_val == target:
            ans.append([item for item in lst])
            return

        if sum_val>target or idx>=len(candidates):
            return

        j = idx+1
        while j<len(candidates) and candidates[j] == candidates[j-1]:
            j+=1

        self.recurSolve(candidates,j,sum_val,target,lst,ans)
        for k in range(1,j-idx+1):
            lst.append(candidates[idx])
            self.recurSolve(candidates,j,sum_val+candidates[idx]*k,target,lst,ans)

        for k in range(1,j-idx+1):
            lst.pop()


    def combinationSum2(self, candidates , target: int) :

        candidates.sort()

        lst = []
        ans = []
        self.recurSolve(candidates,0,0,target,lst,ans)
        return ans