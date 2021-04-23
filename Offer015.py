# -*- coding: utf-8 -*-
# @Time    : 2021-04-23 10:58
# @Author  : zxl
# @FileName: Offer015.py


class Solution:
    def hammingWeight(self, n: int) -> int:

        count = 0
        while n:
            count += n%2
            n//=2
        return count


