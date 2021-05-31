# -*- coding: utf-8 -*-
# @Time    : 2021-05-30 21:30
# @Author  : zxl
# @FileName: 081_3.py



class Solution:
    def search(self, nums , target: int) -> bool:


        lo = 0
        hi = len(nums)-1
        while lo<=hi:

            m = (lo+hi)//2
            if nums[m] == target:
                return True
            m1 = m
            while m1>=lo and nums[m1] == nums[m]:
                m1-=1

            m2 = m
            while m2<=hi and nums[m2] == nums[m]:
                m2+=1

            if m1<lo and m2>hi:
                return False
            if m1<lo :
                lo = m2
            elif m2>hi:
                hi = m1
            else:
                if nums[lo]<=nums[m1]:
                    if target>=nums[lo] and target<=nums[m1]:
                        hi = m1
                    else:
                        lo = m2
                else:
                    if target>=nums[m2] and target<=nums[hi]:
                        lo = m2
                    else:
                        hi = m1
        return False
