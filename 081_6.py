# -*- coding: utf-8 -*-
# @Time    : 2021-08-03 21:18
# @Author  : zxl
# @FileName: 081_6.py



class Solution:
    def search(self, nums , target: int) -> bool:

        l = 0
        h = len(nums)-1

        while l<h:
            m = (l+h)//2

            m1 = m+1
            while m1<h and nums[m1]==nums[m]:
                m1+=1

            if nums[m1]<=nums[h]:
                if target>=nums[m1] and target<=nums[h]:
                    l = m1
                else:
                    h = m

            else:
                if target>=nums[l] and target<=nums[m]:
                    h = m
                else:
                    l = m1


        return nums[l] == target