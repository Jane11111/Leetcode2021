# -*- coding: utf-8 -*-
# @Time    : 2021-08-02 15:25
# @Author  : zxl
# @FileName: 456_2.py


class Solution:
    def find132pattern(self, nums ) -> bool:


        n2 = float('-inf')

        lst = []

        for i in range(len(nums)-1,-1,-1):

            if nums[i]<n2:
                return True

            while len(lst) and nums[i]>lst[-1]:
                n2 = max(n2,lst.pop())
            lst.append(nums[i])
        return False





