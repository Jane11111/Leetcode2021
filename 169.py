# -*- coding: utf-8 -*-
# @Time    : 2021-03-20 10:18
# @Author  : zxl
# @FileName: 169.py


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """


        dic = {}

        l = int(0.5*len(nums))

        for item in nums:
            if item not in dic:
                dic[item] = 0
            dic[item]+=1
            if dic[item] > l:
                return item


