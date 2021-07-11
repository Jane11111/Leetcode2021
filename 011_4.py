# -*- coding: utf-8 -*-
# @Time    : 2021-07-07 10:56
# @Author  : zxl
# @FileName: 011_4.py




class Solution:

    def maxArea(self, height ) -> int:


        l = 0
        r = len(height)-1
        ans = 0
        while l<r:
            ans = max(ans,min(height[l],height[r])*(r-l))
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return ans
