# -*- coding: utf-8 -*-
# @Time    : 2021-03-09 10:35
# @Author  : zxl
# @FileName: 055_2.py

class Solution(object):


    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        if len(nums) <= 1:
            return True

        max_step = 1
        i = 0
        while max_step > 0 and i < len(nums):
            n = nums[i]
            max_step = max(max_step-1,n)
            if i + max_step >= len(nums)-1:
                return True
            i += 1
        return False

obj = Solution()
nums = [2,3,1,1,4]
res = obj.canJump(nums)
print(res)