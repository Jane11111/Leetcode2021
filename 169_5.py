# -*- coding: utf-8 -*-
# @Time    : 2021-06-07 10:35
# @Author  : zxl
# @FileName: 169_5.py




class Solution:
    def majorityElement(self, nums ) -> int:



        if len(nums)<=1:
            return nums[0]

        x = nums[0]
        count = 1
        for i in range(1,len(nums)):
            if count == 0:
                x = nums[i]
                count = 1
                continue
            if nums[i] == x:
                count +=1
            else:
                count-=1
        return x



