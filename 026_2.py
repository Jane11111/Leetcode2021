# -*- coding: utf-8 -*-
# @Time    : 2021-07-11 17:52
# @Author  : zxl
# @FileName: 026_3.py

class Solution:
    def removeDuplicates(self, nums ) -> int:

        i = 0

        while i<len(nums):

            i+=1
            while i<len(nums) and nums[i]==nums[i-1]:
                nums.pop(i)
        return len(nums)


