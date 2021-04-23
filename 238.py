# -*- coding: utf-8 -*-
# @Time    : 2021-04-22 19:27
# @Author  : zxl
# @FileName: 238.py


class Solution:
    def productExceptSelf(self, nums )  :

        n = len(nums)
        l1 = [1 for i in range(n)]
        l2 = [1 for i in range(n)]

        for i in range(1,n):
            l1[i] = l1[i-1]*nums[i-1]
            l2[n-i-1] = l2[n-i]*nums[n-i]

        for i in range(n):
            l1[i]*=l2[i]
        return l1

