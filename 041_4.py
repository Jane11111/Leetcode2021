# -*- coding: utf-8 -*-
# @Time    : 2021-08-02 17:51
# @Author  : zxl
# @FileName: 041_4.py


class Solution:
    def firstMissingPositive(self, nums ) -> int:

        if len(nums) == 0:
            return 1


        nums.insert(0,0)
        n = len(nums)

        i = 0
        while i<len(nums):
            if nums[i]>=n or nums[i]<0 or nums[i] == i or nums[nums[i]] == nums[i]:
                i+=1
                continue

            idx = nums[i]
            nums[i],nums[idx] = nums[idx],nums[i]

        for i in range(1,n):
            if nums[i]!=i:
                return i
        return n


