# -*- coding: utf-8 -*-
# @Time    : 2021-05-30 21:15
# @Author  : zxl
# @FileName: 033_5.py



class Solution:

    def search(self, nums, target: int) -> int:

        lo = 0
        hi = len(nums)-1

        while lo<=hi:

            m = (lo+hi)//2
            if nums[m] == target:
                return m
            if lo==hi:
                return -1

            if nums[lo]<=nums[m]:
                if target>=nums[lo] and target <=nums[m]:
                    hi = m
                else:
                    lo = m+1
            else:
                if target>=nums[m+1] and target<=nums[hi]:
                    lo = m+1
                else:
                    hi = m
        return -1


