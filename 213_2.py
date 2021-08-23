# -*- coding: utf-8 -*-
# @Time    : 2021-08-22 11:45
# @Author  : zxl
# @FileName: 213_2.py



class Solution:
    def rob(self, nums ) -> int:

        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]


        robbed = nums[0]
        no_robbed = 0

        for i in range(1,len(nums)-1):
            old_robbed = robbed
            robbed = max(robbed,no_robbed+nums[i])
            no_robbed = max(old_robbed,no_robbed)


        robbed2 = nums[1]
        no_robbed2 = 0
        for i in range(2,len(nums)):
            old_robbed2 = robbed2
            robbed2 = max(robbed2,no_robbed2+nums[i])
            no_robbed2 = max(no_robbed2,old_robbed2)
        return max(robbed,no_robbed,robbed2,no_robbed2)
