# -*- coding: utf-8 -*-
# @Time    : 2021-05-15 11:41
# @Author  : zxl
# @FileName: 912_bubble_sort.py


# 时间复杂度 O(N^2)
# 空间复杂度 O(1)


class Solution:


    def bubble_sort(self,nums):

        for i in range(len(nums)-1,-1,-1):
            largest_idx = i
            for j in range(i):
                if nums[j]>nums[largest_idx]:
                    largest_idx = j
            nums[i],nums[largest_idx] = nums[largest_idx],nums[i]



    def sortArray(self, nums ) :

        self.bubble_sort(nums)
        return nums
