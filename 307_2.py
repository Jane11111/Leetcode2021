# -*- coding: utf-8 -*-
# @Time    : 2021-06-18 13:54
# @Author  : zxl
# @FileName: 307_2.py

import numpy as np

class NumArray:

    def __init__(self, nums ):

        n = len(nums)
        block_size = int(np.sqrt(n))+1
        block_num = n//block_size + 1
        self.nums = nums
        self.block_size = block_size
        self.block_num = block_num
        self.block_sum = []
        for i in range(block_num):
            self.block_sum.append(sum(nums[i*block_size:(i+1)*block_size]))



    def update(self, index: int, val: int) -> None:

        diff = val-self.nums[index]

        block_id = index//self.block_size
        self.nums[index] = val
        self.block_sum[block_id]+=diff


    def sumRange(self, left: int, right: int) -> int:

        ans = 0

        id1 = left//self.block_size
        id2 = right//self.block_size

        for i in range(id1+1,id2):
            ans += self.block_sum[i]

        for i in range(left,min((id1+1)*self.block_size,right+1)):
            ans+=self.nums[i]

        if id2>id1:
            for i in range(self.block_size*(id2),right):
                ans+=self.nums[i]
        return ans

