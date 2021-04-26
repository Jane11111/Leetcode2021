# -*- coding: utf-8 -*-
# @Time    : 2021-04-25 22:19
# @Author  : zxl
# @FileName: 283_2.py

class Solution:
    def moveZeroes(self, nums ) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        j =0

        for num in nums:
            if num!=0:
                nums[j] = num
                j+=1
        while j<len(nums):
            nums[j] = 0
            j+=1


