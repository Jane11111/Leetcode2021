# -*- coding: utf-8 -*-
# @Time    : 2021-06-23 15:41
# @Author  : zxl
# @FileName: 414.py


class Solution:
    def thirdMax(self, nums) -> int:

        if len(nums)<3:
            return max(nums)

        idx1 = -1
        min_val = float('-inf')
        for i in range(len(nums)):
            if nums[i]>min_val:
                min_val = nums[i]
                idx1 = i

        idx2 = -1
        min_val = float('-inf')
        for i in range(len(nums)):
            if nums[i]!=nums[idx1] and nums[i]>min_val:
                min_val = nums[i]
                idx2 = i
        if idx2 == -1:
            return nums[idx1]

        idx3 = -1
        min_val = float('-inf')
        for i in range(len(nums)):
            if  nums[i]!=nums[idx1] and nums[i]!=nums[idx2] and nums[i]>min_val:
                min_val = nums[i]
                idx3 = i
        if idx3 == -1:
            return nums[idx1]
        return nums[idx3]

