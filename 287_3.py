# -*- coding: utf-8 -*-
# @Time    : 2021-05-14 10:24
# @Author  : zxl
# @FileName: 287_3.py




class Solution:
    def findDuplicate(self, nums ) :

        n = len(nums)

        lo = 1
        hi = n
        while lo<hi:
            mid = (lo+hi)//2

            cnt = 0
            for num in nums:
                if num<=mid:
                    cnt+=1
            if cnt>mid:
                hi = mid
            else:
                lo = mid+1
        return lo
