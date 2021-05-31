# -*- coding: utf-8 -*-
# @Time    : 2021-05-28 15:28
# @Author  : zxl
# @FileName: 198_2.py



class Solution:
    def rob(self, nums ) -> int:

        if len(nums)<1:
            return 0


        arr1 = [0 for i in range(len(nums))]
        arr2 = [0 for i in range(len(nums))]

        arr2[0] = nums[0]
        for i in range(1,len(nums)):
            arr1[i] = max(arr1[i-1],arr2[i-1])
            arr2[i] = arr1[i-1]+nums[i]
        return max(max(arr1),max(arr2))

