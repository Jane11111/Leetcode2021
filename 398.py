# -*- coding: utf-8 -*-
# @Time    : 2021-06-23 14:23
# @Author  : zxl
# @FileName: 398.py

import random
class Solution:

    def __init__(self, nums ):

        self.nums = nums


    def pick(self, target: int) -> int:

        idx = -1
        count = 0
        for i in range(len(self.nums)):
            if self.nums[i] == target:
                p = random.random()
                count+=1
                if p<=(1/count):
                    idx = i
        return idx




