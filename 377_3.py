# -*- coding: utf-8 -*-
# @Time    : 2021-07-13 16:37
# @Author  : zxl
# @FileName: 377_3.py




class Solution:


    def recurSolve(self,nums, sum_val,target,lst,ans):

        if sum_val == target:
            ans.append([item for item in lst])

            return
        if sum_val > target:
            return

        for i in range( len(nums)):
            lst.append(nums[i])
            self.recurSolve(nums, sum_val+nums[i],target,lst,ans)
            lst.pop()

    def combinationSum4(self, nums , target: int) -> int:



        lst = []
        ans = []
        self.recurSolve(nums, 0,target,lst,ans)
        return len(ans)