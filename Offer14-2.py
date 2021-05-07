# -*- coding: utf-8 -*-
# @Time    : 2021-05-06 15:30
# @Author  : zxl
# @FileName: Offer14-2.py


class Solution:
    def cuttingRope(self, n: int) -> int:

        arr = [0, 1, 1]
        for i in range(3, n + 1):
            v = 0
            for j in range(1, i):
                v = max(v, max(arr[j], j) * max(arr[i - j], i - j))
            arr.append(v)
        return arr[n]%1000000007