# -*- coding: utf-8 -*-
# @Time    : 2021-07-12 14:40
# @Author  : zxl
# @FileName: 034_1.py


class Solution:

    def findLeft(self,nums,target):

        l = 0
        h = len(nums)-1

        while l<h:
            m = (l+h)//2

            if target<=nums[m]:
                h = m
            else:
                l = m+1
        if nums[l] == target:
            return l
        return -1

    def findRight(self,nums,target):

        l = 0
        h = len(nums)-1

        while l<h:
            m = (l+h+1)//2
            if target>=nums[m]:
                l = m
            else:
                h = m-1
        if nums[h] == target:
            return h
        return -1

    def searchRange(self, nums , target: int):

        if len(nums) == 0:
            return [-1,-1]

        l = self.findLeft(nums,target)
        r = self.findRight(nums,target)
        return [l,r]
