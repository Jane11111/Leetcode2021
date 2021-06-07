# -*- coding: utf-8 -*-
# @Time    : 2021-06-02 11:22
# @Author  : zxl
# @FileName: 494.py




class Solution:
    def findTargetSumWays(self, nums , target: int) -> int:

        lst = [nums[0],-nums[0]]
        for i in range(1,len(nums)):
            num = nums[i]
            l = len(lst)
            for j in range(l):
                lst.append(lst[j]-num)
                lst[j] += num
        ans = 0
        for i in range(len(lst)):
            if lst[i] == target:
                ans+=1
        return ans






