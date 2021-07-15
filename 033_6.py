# -*- coding: utf-8 -*-
# @Time    : 2021-07-12 13:30
# @Author  : zxl
# @FileName: 033_6.py

class Solution:
    def search(self, nums , target: int) -> int:
        l = 0
        h = len(nums)-1

        while l<h:
            m = (l+h)//2

            if nums[l]<=nums[m]:
                if target>=nums[l] and target <=nums[m]:
                    h = m
                else:
                    l = m+1
            else:
                if target>=nums[m+1] and target <= nums[h]:
                    l = m+1
                else:
                    h = m



        if nums[l] == target:
            return l
        return -1




