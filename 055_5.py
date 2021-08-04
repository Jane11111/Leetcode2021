# -*- coding: utf-8 -*-
# @Time    : 2021-08-03 10:43
# @Author  : zxl
# @FileName: 055_5.py


class Solution:
    def canJump(self, nums ) -> bool:



        if len(nums)<=1:
            return True


        i = 0
        max_len = nums[0]

        while i<=max_len:
            if i>=len(nums)-1:
                return True
            max_len = max(max_len,i+nums[i])
            i+=1
        return False


