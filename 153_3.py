# -*- coding: utf-8 -*-
# @Time    : 2021-05-30 20:44
# @Author  : zxl
# @FileName: 153_3.py


class Solution:

    def recFind(self,nums,i,j):
        if i==j:
            return nums[i]
        if j-i == 1:
            return min(nums[i],nums[j])
        if j-i == 2:
            return min([nums[i],nums[i+1],nums[j]])

        m = (i+j)//2

        if nums[i]<nums[m] and nums[m+1]<nums[j]:
            return min(nums[i],nums[m+1])
        if nums[i]<nums[m]:
            return self.recFind(nums,m+1,j)
        return self.recFind(nums,i,m)

    def findMin(self, nums) -> int:

        ans = self.recFind(nums,0,len(nums)-1)
        return ans




