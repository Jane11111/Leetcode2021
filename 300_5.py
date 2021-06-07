# -*- coding: utf-8 -*-
# @Time    : 2021-06-01 09:30
# @Author  : zxl
# @FileName: 300_5.py




class Solution:
    def lengthOfLIS(self, nums ) -> int:


        n = len(nums)
        lst = [nums[0]]

        for i in range(1,len(nums)):
            num = nums[i]
            if num>lst[-1]:
                lst.append(num)
            else:
                lo = 0
                hi = len(lst)-1
                while lo<hi:

                    m = (lo+hi)//2
                    if lst[m]<num:
                        lo = m+1
                    else:
                        hi = m
                lst[lo] = num
        return len(lst)


