# -*- coding: utf-8 -*-
# @Time    : 2021-07-06 09:55
# @Author  : zxl
# @FileName: 042_7.py


class Solution:
    def trap(self, height) -> int:

        l = 0
        lmax = 0
        r = len(height)-1
        rmax = 0

        ans = 0
        while l<=r:
            lmax = max(lmax,height[l])
            rmax = max(rmax,height[r])
            # 停着的那个指针（r）指向它对应的（右）边的最大值,左边指针直到找到比当前rmax更大的lmax才会被固定，此时l又会指向新的lmax
            if height[l]<height[r]:
                ans += lmax-height[l]
                l+=1
            else:
                ans += rmax-height[r]
                r-=1
        return ans

