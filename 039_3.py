# -*- coding: utf-8 -*-
# @Time    : 2021-05-10 21:15
# @Author  : zxl
# @FileName: 039_3.py


class Solution:


    def recursiveFind(self,nums,idx,target):
        if target == 0:
            return [[]]
        if idx == len(nums) or target<0:
            return []
        ans = []
        for i in range(idx,len(nums)):
            lst = self.recursiveFind(nums,i,target-nums[i])
            for sub_lst in lst:
                sub_lst.insert(0,nums[i])
                ans.append(sub_lst)
        return ans

    def combinationSum(self, candidates , target ) :


        ans = self.recursiveFind(candidates,0,target)
        return ans

obj = Solution()
candidates = [2,3,5]
target = 8
ans = obj.combinationSum(candidates,target)
print(ans)

