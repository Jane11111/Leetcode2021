# -*- coding: utf-8 -*-
# @Time    : 2021-05-18 16:19
# @Author  : zxl
# @FileName: 169_3.py



class Solution:
    def majorityElement(self, nums ) -> int:

        if len(nums) == 1:
            return nums[0]

        x = nums[0]
        c = 1
        i = 1
        while i<len(nums):
            if nums[i] == x:
                c+=1
            else:
                c-=1
                if c == 0:
                    x = nums[i+1]
                    c = 1
                    i+=1
            i+=1
        return x