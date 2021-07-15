# -*- coding: utf-8 -*-
# @Time    : 2021-07-12 17:02
# @Author  : zxl
# @FileName: 041_3.py


class Solution:
    def firstMissingPositive(self, nums ) -> int:

        nums.append(0)


        i = 0

        while i<len(nums):

            if nums[i] == i   or nums[i]>=len(nums) or nums[i]<0 or nums[nums[i]] == nums[i]:
                i+=1
                continue

            tmp = nums[i]
            nums[i],nums[tmp]=nums[tmp],nums[i]

        i = 1
        while i<len(nums):
            if nums[i]!=i:
                return i
            i+=1
        return i

