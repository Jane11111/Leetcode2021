# -*- coding: utf-8 -*-
# @Time    : 2021-04-22 19:37
# @Author  : zxl
# @FileName: 239.py


class Solution:
    def maxSlidingWindow(self, nums , k ) :
        lst = []
        for i in range(k-1):
            if len(lst)==0 or nums[i]<=lst[-1]:
                lst.append(nums[i])
            else:
                while len(lst)>0 and nums[i]>lst[-1]:
                    lst.pop()
                lst.append(nums[i])
        ans = []
        for i in range(0,len(nums)-(k-1)):
            while len(lst)>0 and nums[i+k-1]>lst[-1]:
                lst.pop()
            lst.append(nums[i+k-1])
            ans.append(lst[0])
            if lst[0] == nums[i]:
                lst.pop(0)


        return ans

