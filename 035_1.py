# -*- coding: utf-8 -*-
# @Time    : 2021-07-12 15:10
# @Author  : zxl
# @FileName: 035_1.py

class Solution:
    def searchInsert(self, nums , target: int) -> int:

        if len(nums) == 0 or target>nums[-1]:
            return len(nums)


        l = 0
        h = len(nums)-1

        while l<h:

            m = (l+h)//2

            if target<= nums[m]:
                h = m
            else:
                l = m+1
        return l



