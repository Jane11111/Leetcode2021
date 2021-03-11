# -*- coding: utf-8 -*-
# @Time    : 2021-03-10 19:50
# @Author  : zxl
# @FileName: 287.py


class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for item in nums:

            if item in dic:
                return item
            dic[item] = True

