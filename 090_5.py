# -*- coding: utf-8 -*-
# @Time    : 2021-08-04 13:44
# @Author  : zxl
# @FileName: 090_5.py


class Solution:

    def recFind(self,nums,idx,lst,ans):
        if idx == len(nums):
            ans.append([item for item in lst])
            return

        i = idx+1
        while i<len(nums) and nums[i] == nums[i-1]:
            i+=1

        count = i-idx
        self.recFind(nums,i,lst,ans)
        for k in range(1,count+1):
            lst.append(nums[idx])
            self.recFind(nums,i,lst,ans)

        for k in range(1,count+1):
            lst.pop()


    def subsetsWithDup(self, nums ) :

        nums.sort()
        lst = []
        ans = []
        self.recFind(nums,0,lst,ans)
        return ans

