# -*- coding: utf-8 -*-
# @Time    : 2021-05-06 14:54
# @Author  : zxl
# @FileName: 560_2.py



class Solution:
    def subarraySum(self, nums , k )  :

        dic = {}
        dic[0] = 1
        val = 0
        count = 0
        for i in range(len(nums)):

            val += nums[i]


            if val-k in dic :
                count+=dic[val-k]

            if val not in dic:
                dic[val] = 0
            dic[val] += 1
        return count

