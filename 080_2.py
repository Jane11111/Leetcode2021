# -*- coding: utf-8 -*-
# @Time    : 2021-08-03 21:05
# @Author  : zxl
# @FileName: 080_2.py

class Solution:
    def removeDuplicates(self, nums ) -> int:


        p = -1
        i = 0
        count = 0
        while i<len(nums):
            cur_num = nums[i]

            nums[p+1],nums[i] = nums[i],nums[p+1]
            count+=1
            p+=1
            i+=1
            if i<len(nums) and nums[i] == cur_num:
                nums[p+1],nums[i] = nums[i], nums[p+1]
                p+=1
                i+=1
                count+=1
                while i<len(nums) and nums[i] == cur_num:
                    i+=1
        return count





