# -*- coding: utf-8 -*-
# @Time    : 2021-04-24 22:10
# @Author  : zxl
# @FileName: Offer042.py


class Solution:
    def maxSubArray(self, nums ) -> int:

        i= 0

        max_val = float('-inf')


        while i<len(nums):


            while i < len(nums) and nums[i] < 0:
                max_val = max(max_val, nums[i])
                i += 1
            if i>=len(nums):
                continue

            cur_val = nums[i] # 一定是正数
            max_val = max(max_val,cur_val)
            i+=1
            while i<len(nums) and cur_val+nums[i]>0:
                cur_val+=nums[i]
                max_val = max(max_val,cur_val)
                i+=1
        return max_val

