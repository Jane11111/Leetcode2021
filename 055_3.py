# -*- coding: utf-8 -*-
# @Time    : 2021-07-14 13:27
# @Author  : zxl
# @FileName: 055_3.py

class Solution:
    def canJump(self, nums ) -> bool:

        max_len = nums[0]
        i = 0

        while i<=max_len and max_len<len(nums):

            max_len = max(max_len,i+nums[i])
            i+=1
        return max_len >=len(nums)-1



