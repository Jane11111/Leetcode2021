# -*- coding: utf-8 -*-
# @Time    : 2021-05-14 09:49
# @Author  : zxl
# @FileName: 287_2.py




class Solution:
    def findDuplicate(self, nums ) :


        i = 0
        while True:
            num = nums[i]
            if nums[num] == num:
                return num
            nums[i] = nums[num]
            nums[num] = num

