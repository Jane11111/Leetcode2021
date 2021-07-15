# -*- coding: utf-8 -*-
# @Time    : 2021-07-12 10:53
# @Author  : zxl
# @FileName: 031_2.py



class Solution:
    def nextPermutation(self, nums ) -> None:


        n = len(nums)

        i = n-1
        while i-1>=0 and nums[i-1]>=nums[i]:
            i-=1


        if i-1>=0:

            idx = n-1
            while nums[idx]<=nums[i-1]:
                idx-=1
            nums[idx], nums[i-1] = nums[i-1],nums[idx]

        j = n-1
        while i<j:
            nums[i],nums[j] = nums[j],nums[i]
            i+=1
            j-=1


