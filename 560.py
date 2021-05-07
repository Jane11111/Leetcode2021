# -*- coding: utf-8 -*-
# @Time    : 2021-05-06 14:36
# @Author  : zxl
# @FileName: 560.py


class Solution:
    def subarraySum(self, nums , k )  :

        dic = {}
        dic[0] = 1
        val = 0
        count = 0
        for i in range(len(nums)):

            val+=nums[i]
            if val not in dic:
                dic[val] = 0
            dic[val]+=1


            if val-k in dic :
                if k == 0:
                    count+=(dic[val-k]-1)
                else:
                    count+=dic[val-k]
        return count




