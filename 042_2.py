# -*- coding: utf-8 -*-
# @Time    : 2021-05-17 22:07
# @Author  : zxl
# @FileName: 042_2.py


class Solution:
    def trap(self, height) -> int:

        arr1 = [0 for i in range(len(height))]
        arr2 = [0 for i in range(len(height))]

        max_height = 0
        for i in range(len(height)):
            max_height = max(max_height,height[i])
            arr1[i] = max_height

        max_height = 0
        for i in range(len(height)-1,-1,-1):
            max_height = max(max_height,height[i])
            arr2[i] = max_height

        ans = 0
        for i in range(len(height)):
            ans+= min(arr1[i],arr2[i])-height[i]
        return ans

