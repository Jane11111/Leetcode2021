# -*- coding: utf-8 -*-
# @Time    : 2021-07-14 13:35
# @Author  : zxl
# @FileName: 055_4.py



class Solution:
    def canJump(self, nums ) -> bool:

        max_len = nums[0]

        for i in range(len(nums)):
            if i>max_len:
                return False
            max_len = max(max_len,i+nums[i])
        return True
