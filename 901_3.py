# -*- coding: utf-8 -*-
# @Time    : 2021-07-31 10:35
# @Author  : zxl
# @FileName: 901_3.py

class StockSpanner:

    def __init__(self):
        self.lst = []
        self.dp = []


    def next(self, price: int) -> int:

        self.lst.append(price)

        i = len(self.lst)-1

        while i>=0 and self.lst[i]<=price:
            i -= self.dp[i]

        count = len(self.lst)-i-1
        self.dp.append(count)
        return count







