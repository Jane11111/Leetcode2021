# -*- coding: utf-8 -*-
# @Time    : 2021-06-23 15:53
# @Author  : zxl
# @FileName: 414_2.py




class Solution:
    def thirdMax(self, nums) -> int:

        nums1 = float('-inf')
        nums2 = float('-inf')
        nums3 = float('-inf')

        for num in nums:
            if num>nums1:
                nums3,nums2,nums1 = nums2,nums1,num
            elif num!=nums1 and num>nums2:
                nums3,nums2 = nums2,num
            elif num!= nums1 and num!=nums2 and num>nums3:
                nums3 = num
        if nums3!=float('-inf'):
            return nums3
        return nums1



