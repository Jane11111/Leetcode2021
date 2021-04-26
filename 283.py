# -*- coding: utf-8 -*-
# @Time    : 2021-04-25 22:14
# @Author  : zxl
# @FileName: 283.py




class Solution:
    def moveZeroes(self, nums ) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        i = 0
        n = len(nums)
        while n>0:
            n-=1
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
            else:
                i+=1
