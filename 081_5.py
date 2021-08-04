# -*- coding: utf-8 -*-
# @Time    : 2021-08-03 09:33
# @Author  : zxl
# @FileName: 081_5.py



class Solution:
    def search(self, nums , target: int) -> bool:

        i = 0
        j = len(nums)-1


        while i<j:

            m = (i+j)//2

            m1 = m+1
            while m1<j and nums[m1] == nums[m1-1]:
                m1+=1

            if nums[m1]<=nums[j]:
                if target>=nums[m1] and target<=nums[j]:
                    i = m1
                else:
                    j = m
            else:
                if target>=nums[i] and target <= nums[m]:
                    j = m
                else:
                    i = m1
        return nums[i] == target

