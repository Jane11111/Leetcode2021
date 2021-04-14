# -*- coding: utf-8 -*-
# @Time    : 2021-04-07 09:27
# @Author  : zxl
# @FileName: 901_2.py


class StockSpanner:

    def __init__(self):

        self.lst = []

    def next(self, price: int) -> int:


        if len(self.lst) == 0 or price<self.lst[-1][0]:
            self.lst.append((price,1))
            # self.val.append(1)
            return 1
        else:
            count = 1
            while len(self.lst) > 0 and price>=self.lst[-1][0]:
                count += self.lst[-1][1]
                # self.val.pop()
                self.lst.pop()
            self.lst.append((price,count))
            # self.val.append(count)
            return count


