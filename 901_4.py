# -*- coding: utf-8 -*-
# @Time    : 2021-07-31 10:48
# @Author  : zxl
# @FileName: 901_4.py

class StockSpanner:

    def __init__(self):

        self.lst = []
        self.val = []


    def next(self, price: int) -> int:


        count = 1

        while len(self.lst) and price>=self.lst[-1]:

            p = self.lst.pop()
            v = self.val.pop()
            count+=v
        self.lst.append(price)
        self.val.append(count)
        return count






