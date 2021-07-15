# -*- coding: utf-8 -*-
# @Time    : 2021-07-11 17:59
# @Author  : zxl
# @FileName: 026_3.py



class Solution:
    def removeDuplicates(self, nums ) -> int:

        i = 0
        p = -1
        count = 0

        while i<len(nums):

            count +=1

            j = i+1
            while j<len(nums) and nums[j] == nums[i]:
                j+=1

            nums[p+1], nums[j-1] = nums[j-1],nums[p+1]
            p+=1

            i = j
        return count

