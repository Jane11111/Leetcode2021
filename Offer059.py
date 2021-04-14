# -*- coding: utf-8 -*-
# @Time    : 2021-04-14 13:08
# @Author  : zxl
# @FileName: Offer059.py


class MaxQueue:

    def __init__(self):
        self.queue = []
        self.max_val = float('-inf')




    def max_value(self) -> int:
        if len(self.queue) == 0:
            return -1
        return self.max_val



    def push_back(self, value: int) -> None:

        self.max_val = max(self.max_val,value)
        self.queue.append(value)



    def pop_front(self) -> int:

        if len(self.queue) == 0:
            return -1

        if self.max_val == self.queue[0]:
            self.max_val = float('-inf')
            for i in range(1,len(self.queue)):
                self.max_val = max(self.max_val,self.queue[i])
        return self.queue.pop(0)




