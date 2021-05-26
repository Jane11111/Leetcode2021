# -*- coding: utf-8 -*-
# @Time    : 2021-05-16 21:57
# @Author  : zxl
# @FileName: 264.py



class Solution:
    def nthUglyNumber(self, n: int) -> int:

        lst = [1]
        p2 = 0
        p3 = 0
        p5 = 0
        for i in range(1,n ):
            num = min(lst[p2]*2,lst[p3]*3,lst[p5]*5)
            lst.append(num)
            if num%2 == 0:
                p2+=1
            if num%3 == 0:
                p3 +=1
            if num%5 == 0:
                p5 += 1
        return lst[n-1]