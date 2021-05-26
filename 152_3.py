# -*- coding: utf-8 -*-
# @Time    : 2021-05-13 13:20
# @Author  : zxl
# @FileName: 152_3.py



class Solution:
    def maxProduct(self, nums ) -> int:

        n = len(nums)
        dp_min = [0 for i in range(n)]
        dp_max = [0 for i in range(n)]

        dp_min[0] = nums[0]
        dp_max[0] = nums[0]



        for i in range(1,n):
            v1 = dp_min[i-1]*nums[i]
            v2 = dp_max[i-1]*nums[i]

            dp_min[i] = min(v1,v2,nums[i])
            dp_max[i] = max(v1,v2,nums[i])
        return max(dp_max)



