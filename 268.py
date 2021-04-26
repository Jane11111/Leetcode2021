# -*- coding: utf-8 -*-
# @Time    : 2021-04-25 22:04
# @Author  : zxl
# @FileName: 268.py

class Solution:
    def missingNumber(self, nums ) -> int:

        n = len(nums)

        a = 0
        for i in range(n+1):
            a^=i

        for num in nums:
            a^=num

        return a
