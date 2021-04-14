# -*- coding: utf-8 -*-
# @Time    : 2021-04-14 21:16
# @Author  : zxl
# @FileName: Offer049.py


class Solution:
    def nthUglyNumber(self, n: int) -> int:

        arr = [1]
        p2 = 0
        p3 = 0
        p5 = 0
        while len(arr)<n:
            v2 = arr[p2]*2
            v3 = arr[p3]*3
            v5 = arr[p5]*5

            min_val = min([v2,v3,v5])
            if min_val%2 == 0:
                p2+=1
            if min_val%3 == 0:
                p3+=1
            if min_val%5 == 0:
                p5+=1
            arr.append(min_val)

        return arr[n-1]