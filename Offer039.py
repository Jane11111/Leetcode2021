# -*- coding: utf-8 -*-
# @Time    : 2021-04-24 22:02
# @Author  : zxl
# @FileName: Offer039.py


class Solution:
    def majorityElement(self, nums) -> int:

        x = nums[0]
        count = 1
        i = 1
        while i<len(nums):
            if nums[i] == x:
                count+=1
            else:
                count -=1
            i+=1
            if count == 0:
                x = nums[i]
                count=1
                i+=1
        return x
