# -*- coding: utf-8 -*-
# @Time    : 2021-07-13 16:22
# @Author  : zxl
# @FileName: 039_5.py


class Solution:


    def recurFind(self,nums,idx,target,sum_val,lst,ans):
        if sum_val == target:
            ans.append([item for item in lst])
            return
        if sum_val>target:
            return

        for i in range(idx,len(nums)):
            lst.append(nums[i])
            self.recurFind(nums,i,target,sum_val+nums[i],lst,ans)
            lst.pop()



    def combinationSum(self, candidates , target: int) :

        lst = []
        ans = []
        self.recurFind(candidates,0,target,0,lst,ans)
        return ans



