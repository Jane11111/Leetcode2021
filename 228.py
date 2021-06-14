# -*- coding: utf-8 -*-
# @Time    : 2021-06-13 16:18
# @Author  : zxl
# @FileName: 228.py



class Solution:
    def summaryRanges(self, nums ) :


        ans = []

        i = 0

        while i<len(nums):
            j = i+1
            while j<len(nums) and nums[j]-nums[j-1] == 1:
                j+=1

            if j-i == 1:
                ans.append(str(nums[i]))
            else:
                ans.append(str(nums[i])+'->'+str(nums[j-1]))
            i = j
        return ans