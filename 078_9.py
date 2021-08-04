# -*- coding: utf-8 -*-
# @Time    : 2021-08-03 19:57
# @Author  : zxl
# @FileName: 078_9.py




class Solution:

    def recFind(self,nums,idx,lst,ans):

        if idx == len(nums):
            ans.append([item for item in lst])
            return

        self.recFind(nums,idx+1,lst,ans)
        lst.append(nums[idx])
        self.recFind(nums,idx+1,lst,ans)
        lst.pop()

    def subsets(self, nums ) :
        lst = []
        ans = []
        self.recFind(nums,0,lst,ans)
        return ans

