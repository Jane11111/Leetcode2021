# -*- coding: utf-8 -*-
# @Time    : 2021-07-06 09:21
# @Author  : zxl
# @FileName: 042_5.py

class Solution:
    def trap(self, height ) -> int:

        idx = -1
        max_h = 0
        for i in range(len(height)):
            if height[i]>=max_h:
                idx = i
                max_h = height[i]
        ans = 0

        left_max = 0
        for i in range(idx):
            left_max = max(left_max,height[i])
            ans+= left_max-height[i]
        right_max = 0
        for i in range(len(height)-1,idx,-1):
            right_max = max(right_max,height[i])
            ans+= right_max-height[i]
        return ans



