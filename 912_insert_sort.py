# -*- coding: utf-8 -*-
# @Time    : 2021-05-15 11:36
# @Author  : zxl
# @FileName: 912_insert_sort.py

# 时间复杂度 O(N^2)
# 空间复杂度 O(1)

class Solution:


    def insert_sort(self,nums):

        for i in range(1,len(nums)):
            for j in range(i-1,-1,-1):
                if nums[j+1]<nums[j]:
                    nums[j],nums[j+1]= nums[j+1],nums[j]
                else:
                    break



    def sortArray(self, nums ) :


        self.insert_sort(nums)
        return nums

