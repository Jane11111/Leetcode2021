# -*- coding: utf-8 -*-
# @Time    : 2021-07-12 10:22
# @Author  : zxl
# @FileName: 030_1.py


class Solution:
    def nextPermutation(self, nums ) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)

        i = n-1
        while i-1>=0 and nums[i-1]>=nums[i]:
            i-=1

        if i ==0:
            i = 0
            j = n-1
            while i<j:
                nums[i],nums[j] = nums[j],nums[i]
                i+=1
                j-=1
        else:

            idx = i-1
            j = n-1
            while i<j:
                nums[i],nums[j] = nums[j],nums[i]
                i+=1
                j-=1

            i = idx+1
            while i<n and nums[i]<=nums[idx]:
                i+=1
            nums[idx],nums[i] = nums[i],nums[idx]

            while i+1<n and nums[i]>nums[i+1]:
                nums[i],nums[i+1] = nums[i+1],nums[i]
                i+=1








