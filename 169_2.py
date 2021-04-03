# -*- coding: utf-8 -*-
# @Time    : 2021-03-20 10:27
# @Author  : zxl
# @FileName: 169_2.py


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        count = 1
        ans = nums[0]
        for i in range(1,len(nums)):
            if count == 0:
                ans = nums[i]
                count=1
                continue
            if nums[i] == ans:
                count+=1
            else:
                count-=1

        return ans