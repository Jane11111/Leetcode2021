# -*- coding: utf-8 -*-
# @Time    : 2021-03-06 15:23
# @Author  : zxl
# @FileName: 698.py


class Solution(object):

    def C(self,nums,m):

        if m > len(nums) or m <= 0:
            return []
        res = []
        for i in range(len(nums)):

            if m == 1:
                res.append([nums[i]])
            else:
                sub_res = self.C(nums[i+1:],m-1)
                for item in sub_res:
                    item.append(nums[i])
                    res.append(item)
        return res



    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        # for i in range(1,len(nums)-k+1,1):


