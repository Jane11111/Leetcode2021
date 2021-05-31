# -*- coding: utf-8 -*-
# @Time    : 2021-05-30 21:09
# @Author  : zxl
# @FileName: 033_4.py



class Solution:

    def biSearch(self,nums,i,j,target):

        if i>j or (i==j and nums[i]!=target):
            return -1
        if i==j and nums[i] == target:
            return i

        m = (i+j)//2
        lo = i
        hi = j

        if nums[i]<=nums[m]:
            if target>=nums[i] and target<=nums[m]:
                hi = m
            else:
                lo = m+1
        else:
            if target>=nums[m+1] and target<=nums[j]:
                lo = m+1
            else:
                hi = m

        return self.biSearch(nums,lo,hi,target)


    def search(self, nums, target: int) -> int:

        ans = self.biSearch(nums,0,len(nums)-1,target)
        return ans

