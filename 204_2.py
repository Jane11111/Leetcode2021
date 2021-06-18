# -*- coding: utf-8 -*-
# @Time    : 2021-06-18 13:16
# @Author  : zxl
# @FileName: 205.py




class Solution:



    def countPrimes(self, n: int) -> int:


        if n <=2 :
            return 0


        lst = [1 for i in range(n)]
        lst[0] = 0
        lst[1] = 0
        lst[2] = True
        for i in range(2,n):
            if lst[i]:
                for j in range(2,n):
                    if i*j>=n:
                        break
                    lst[i*j] = 0
        return sum(lst)



