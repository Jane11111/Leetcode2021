# -*- coding: utf-8 -*-
# @Time    : 2021-03-11 22:31
# @Author  : zxl
# @FileName: 153.py


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        ans = nums[0]
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                return nums[i]
        return ans