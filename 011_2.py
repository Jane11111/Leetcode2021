# -*- coding: utf-8 -*-
# @Time    : 2021-07-07 10:41
# @Author  : zxl
# @FileName: 011_2.py



class Solution:
    def maxArea(self, height ) -> int:

        ans = 0
        n = len(height)
        for i in range(n):
            for j in range(i+1,n):
                ans = max(ans, min(height[i],height[j])*(j-i))
        return ans

