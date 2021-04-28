# -*- coding: utf-8 -*-
# @Time    : 2021-04-28 20:51
# @Author  : zxl
# @FileName: 041.py


class Solution:
    def firstMissingPositive(self, nums) :

        nums.append(0)

        n = len(nums)

        i = 0
        while i<n:
            if nums[i] >=0 and nums[i]<n and nums[nums[i]]!=nums[i]:
                tmp = nums[nums[i]]
                nums[nums[i]] = nums[i]
                nums[i] = tmp
            else:
                i +=1
        for i in range(1,n):
            if nums[i]!=i:
                return i
        return n