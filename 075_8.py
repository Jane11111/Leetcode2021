# -*- coding: utf-8 -*-
# @Time    : 2021-08-03 18:05
# @Author  : zxl
# @FileName: 075_8.py



class Solution:
    def sortColors(self, nums ) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """


        p = -1
        q = len(nums)-1

        while q>=0 and nums[q] == 2:
            q-=1

        i = 0
        while i<=q:

            if nums[i] == 0:
                nums[p+1],nums[i] = nums[i],nums[p+1]
                p+=1
                i+=1
            elif nums[i] == 2:
                nums[i],nums[q] = nums[q],nums[i]
                q-=1
                while q>=i and nums[q] == 2:
                    q-=1
            else:
                i+=1


