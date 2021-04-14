# -*- coding: utf-8 -*-
# @Time    : 2021-04-14 13:51
# @Author  : zxl
# @FileName: Offer0302.py

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.st = []
        self.min_val = float('inf')


    def push(self, x: int) -> None:
        self.min_val = min(self.min_val,x)
        self.st.append(self.min_val)
        self.st.append(x)


    def pop(self) -> None:

        self.st.pop()
        self.st.pop()
        self.min_val= self.st[-2] if len(self.st)>0 else float('inf')


    def top(self) -> int:
        return self.st[-1]


    def getMin(self) -> int:
        return self.min_val

