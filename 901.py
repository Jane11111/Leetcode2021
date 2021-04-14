# -*- coding: utf-8 -*-
# @Time    : 2021-04-06 23:12
# @Author  : zxl
# @FileName: 901.py


class StockSpanner:

    def __init__(self):

        self.lst = []
        self.val = []

    def next(self, price: int) -> int:


        if len(self.lst) == 0 or price<self.lst[-1]:
            self.lst.append(price)
            self.val.append(1)
            return 1
        else:
            count = 1
            while len(self.lst) > 0 and price>=self.lst[-1]:
                count += self.val[-1]
                self.val.pop()
                self.lst.pop()
            self.lst.append(price)
            self.val.append(count)
            return count




# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)