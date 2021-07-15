# -*- coding: utf-8 -*-
# @Time    : 2021-07-11 18:08
# @Author  : zxl
# @FileName: 027_2.py


class Solution:
    def removeElement(self, nums , val: int) -> int:

        count = 0
        p = -1
        i = 0
        while i<len(nums):

            if nums[i] == val:
                if p == -1:
                    p = i
            else:
                count+=1
                if p!=-1:
                    nums[p] = nums[i]
                    p+=1
            i+=1
        return count