# -*- coding: utf-8 -*-
# @Time    : 2021-06-15 20:46
# @Author  : zxl
# @FileName: 303.py



class NumArray:

    def __init__(self, nums ):

        arr = [0 for i in range(len(nums))]
        arr[0] = nums[0] if len(nums)>=1 else 0
        for i in range(1,len(nums)):
            arr[i] = arr[i-1]+nums[i]
        self.arr = arr
        self.nums = nums



    def sumRange(self, left: int, right: int) -> int:

        l = 0 if left == 0 else self.arr[left-1]

        return self.arr[right]-l

