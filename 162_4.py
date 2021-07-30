# -*- coding: utf-8 -*-
# @Time    : 2021-07-26 21:25
# @Author  : zxl
# @FileName: 162_4.py



class Solution:
    def findPeakElement(self, nums ) -> int:


        l = 0
        h = len(nums)-1

        while l<h:
            m = (l+h)//2

            if nums[m]>nums[m+1]:
                h = m
            else:
                l = m+1
        return l




