# -*- coding: utf-8 -*-
# @Time    : 2021-03-02 13:43
# @Author  : zxl
# @FileName: 035.py


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        i = 0
        while i < len(nums) and nums[i]<target:
            i += 1
        return i


