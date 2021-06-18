# -*- coding: utf-8 -*-
# @Time    : 2021-06-18 13:44
# @Author  : zxl
# @FileName: 307.py

class NumArray:

    def __init__(self, nums ):

        self.nums = nums

        self.sums = [i for i in nums]
        for i in range(1,len(nums)):
            self.sums[i]+=self.sums[i-1]


    def update(self, index: int, val: int) -> None:
        diff = val-self.nums[index]
        self.nums[index]=val
        for i in range(index,len(self.sums)):
            self.sums[i]+=diff



    def sumRange(self, left: int, right: int) -> int:

        l = 0
        if left>0:
            l = self.sums[left-1]
        ans = self.sums[right]-l
        return ans




