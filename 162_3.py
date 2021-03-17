# -*- coding: utf-8 -*-
# @Time    : 2021-03-12 10:16
# @Author  : zxl
# @FileName: 162_3.py



class Solution(object):


    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        i = 0
        j = len(nums)-1
        while i<=j:
            if i==j:
                return i
            m = (i+j)//2
            if nums[m]>nums[m+1]:
                j = m
            else:
                i=m+1
        return -1

obj = Solution()
nums = [1,2,1,3,5,6,4]
ans= obj.findPeakElement(nums)
print(ans)
