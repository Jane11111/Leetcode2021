# -*- coding: utf-8 -*-
# @Time    : 2021-05-17 22:24
# @Author  : zxl
# @FileName: 042_4.py



class Solution(object):




    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """


        idx = 0
        for i in range(len(height)):
            if height[i]>height[idx]:
                idx = i

        ans = 0
        left_max = 0
        for i in range(idx):
            left_max = max(height[i],left_max)
            ans+=left_max-height[i]
        right_max = 0
        for i in range(len(height)-1,idx,-1):
            right_max = max(right_max,height[i])
            ans+=right_max-height[i]
        return ans


