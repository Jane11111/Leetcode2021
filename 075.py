# -*- coding: utf-8 -*-
# @Time    : 2021-03-10 18:22
# @Author  : zxl
# @FileName: 075.py

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        lst = [0,0,0]
        for i in nums:
            lst[i]+=1
        for i in range(len(nums)):
            if i <lst[0]:
                nums[i] = 0
            elif i<lst[0]+lst[1]:
                nums[i] = 1
            else:
                nums[i] = 2


obj = Solution()
nums = [2,0,2,1,1,0]
ans = obj.sortColors(nums)
print(nums)