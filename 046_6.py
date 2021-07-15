# -*- coding: utf-8 -*-
# @Time    : 2021-07-13 13:42
# @Author  : zxl
# @FileName: 046_6.py

class Solution:

    def recurFind(self,nums,used,lst,ans):
        if len(lst) == len(nums):
            ans.append([item for item in lst])
            return

        for i in range(len(nums)):
            if not used[i]:
                lst.append(nums[i])
                used[i] = True
                self.recurFind(nums,used,lst,ans)
                used[i] = False
                lst.pop()



    def permute(self, nums ) :


        used = {i:False for i in range(len(nums))}
        lst = []
        ans = []
        self.recurFind(nums,used,lst,ans)
        return ans



