# -*- coding: utf-8 -*-
# @Time    : 2021-06-22 17:56
# @Author  : zxl
# @FileName: 384_2.py



import random
class Solution:

    def __init__(self, nums ):

        self.origin_nums = [item for item in nums]
        self.nums = [item for item in nums]




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


        for i in range(len(self.nums)):
            idx = random.randrange(i,len(self.nums))
            self.nums[i],self.nums[idx] = self.nums[idx],self.nums[i]
        return self.nums





