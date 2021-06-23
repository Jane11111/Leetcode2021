# -*- coding: utf-8 -*-
# @Time    : 2021-06-22 17:50
# @Author  : zxl
# @FileName: 384.py


import random
class Solution:

    def __init__(self, nums ):

        self.origin_nums = nums
        self. nums = [item for item in self.origin_nums]


    def reset(self) :
        """
        Resets the array to its original configuration and return it.
        """
        self.nums = [item for item in self.origin_nums]
        return self.nums



    def shuffle(self) :
        """
        Returns a random shuffling of the array.
        """
        random.shuffle(self.nums)
        return self.nums


