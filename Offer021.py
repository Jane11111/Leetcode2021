# -*- coding: utf-8 -*-
# @Time    : 2021-04-23 12:57
# @Author  : zxl
# @FileName: Offer021.py


class Solution:
    def exchange(self, nums ) :

        if len(nums) == 0:
            return nums
        j = len(nums)-1
        while j>=0 and nums[j]%2==0:
            j-=1

        p = -1
        for i in range(0,j):
            if nums[i]%2 == 1:
                nums[p+1],nums[i] = nums[i],nums[p+1]
                p+=1
        nums[p+1],nums[j] = nums[j],nums[p+1]
        return nums

