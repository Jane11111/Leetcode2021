# -*- coding: utf-8 -*-
# @Time    : 2021-05-07 15:35
# @Author  : zxl
# @FileName: 146_2.py

class DNode():

    def __init__(self,key,value,left = None,right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right

class LRUCache:

    def __init__(self, capacity: int):

        p = DNode(-1,-1)
        self.head = p
        self.tail = p
        self.capacity = capacity
        self.count = 0
        self.item_dic = {}
        self.freq_dic = {} # 存放某个freq对应的最近使用的pointer



    def get(self, key: int) -> int:

        pass



    def put(self, key: int, value: int) -> None:

        pass

