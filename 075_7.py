# -*- coding: utf-8 -*-
# @Time    : 2021-07-14 18:44
# @Author  : zxl
# @FileName: 075_7.py


class Solution:
    def sortColors(self, nums ) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        p1 = 0
        p2 = n-1
        while p2>=0 and nums[p2] == 2:
            p2-=1

        i = 0
        while i <=p2:

            if nums[i] == 0:
                nums[p1] = 0
                p1+=1
                i+=1
            elif nums[i] == 2:

                nums[i],nums[p2] = nums[p2],nums[i]
                p2-=1
            else:
                i+=1
            while p2>=0 and nums[p2] == 2: # p2指向的永远都不是2
                p2-=1

        for i in range(p1,p2+1):
            nums[i] = 1

