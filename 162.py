# -*- coding: utf-8 -*-
# @Time    : 2021-03-12 09:55
# @Author  : zxl
# @FileName: 162.py


class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 1:
            return 0

        for i in range(len(nums)):

            if i == 0:
                if i+1 < len(nums) and nums[i+1]<nums[i]:
                    return i
            elif i == len(nums)-1:
                if i-1>=0 and nums[i-1]<nums[i]:
                    return i
            else:
                if nums[i]> nums[i-1] and nums[i] > nums[i+1]:
                    return i

