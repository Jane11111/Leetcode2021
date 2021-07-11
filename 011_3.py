# -*- coding: utf-8 -*-
# @Time    : 2021-07-07 10:45
# @Author  : zxl
# @FileName: 011_3.py




class Solution:
    def maxArea(self, height ) -> int:

        n = len(height)
        arr = [i for i in range(n)]

        idx = n-1
        for i in range(n-2,-1,-1):

            arr[i] = idx
            if height[i]>height[idx]:
                idx = i

        ans = 0
        for i in range(n):

            idx = arr[i]
            while idx<n:
                ans = max(ans,min(height[idx],height[i])*(idx-i))
                idx = arr[idx] if idx<n-1 else idx+1
        return ans



