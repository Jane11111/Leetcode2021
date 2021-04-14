# -*- coding: utf-8 -*-
# @Time    : 2021-04-14 13:37
# @Author  : zxl
# @FileName: Offer059_2.py



class MaxQueue:

    def __init__(self):

        self.queue = []
        self.st = []




    def max_value(self) -> int:

        if len(self.st) > 0:
            return self.st[0]
        return -1




    def push_back(self, value: int) -> None:
        self.queue.append(value)
        while len(self.st)>0 and value>self.st[-1]:
            self.st.pop()
        self.st.append(value)




    def pop_front(self) -> int:
        if len(self.queue) == 0:
            return -1

        if self.queue[0] == self.st[0]:
            self.st.pop(0)
        return self.queue.pop(0)

