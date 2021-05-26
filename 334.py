# -*- coding: utf-8 -*-
# @Time    : 2021-05-24 17:11
# @Author  : zxl
# @FileName: 334.py



class Solution:
    def increasingTriplet(self, nums ) -> bool:

        if len(nums)<3:
            return False

        small = float('inf')
        mid  = float('inf')
        for num in nums:
            if num<small:
                small = num
            elif num > small and num<mid:
                mid = num
            elif num>mid:
                return True
        return False



