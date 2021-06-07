# -*- coding: utf-8 -*-
# @Time    : 2021-06-02 11:53
# @Author  : zxl
# @FileName: 494_2.py



class Solution:
    def findTargetSumWays(self, nums , target: int) -> int:


        dic = {}
        dic[nums[0]] = 1
        if -nums[0] not in dic:
            dic[-nums[0]] = 1
        else:
            dic[-nums[0]]+=1

        for i in range(1,len(nums)):
            num = nums[i]

            new_dic = {}
            for k in dic:
                if k+num not in new_dic:
                    new_dic[k+num] = dic[k]
                else:
                    new_dic[k+num] +=dic[k]
                if k-num not in new_dic:
                    new_dic[k-num] = dic[k]
                else:
                    new_dic[k-num] += dic[k]
            dic = new_dic
        ans = 0
        if target in dic:
            ans = dic[target]
        return ans
