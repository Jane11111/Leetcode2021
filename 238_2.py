# -*- coding: utf-8 -*-
# @Time    : 2021-05-14 13:55
# @Author  : zxl
# @FileName: 238_2.py




class Solution:
    def productExceptSelf(self, nums ) :

        ans = [1 for i in range(len(nums))]

        left = 1
        for i in range(0,len(nums)):
            ans[i]*= left
            left*=nums[i]

        right = 1
        for i in range(len(nums)-1,-1,-1):
            ans[i]*=right
            right*=nums[i]
        return ans