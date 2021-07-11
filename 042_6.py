# -*- coding: utf-8 -*-
# @Time    : 2021-07-06 09:24
# @Author  : zxl
# @FileName: 042_6.py


class Solution:
    def trap(self, height) -> int:

        lst = []
        ans = 0

        for i in range(len(height)):

            while len(lst)>0 and height[i]>=height[lst[-1]]:
                hidx = lst.pop()
                if len(lst):
                    lidx = lst[-1]
                    ans+= (min(height[lidx],height[i])-height[hidx])*(i-lidx-1)

            lst.append(i)
        return ans


