# -*- coding: utf-8 -*-
# @Time    : 2021-04-14 09:16
# @Author  : zxl
# @FileName: 146.py


class DNode():
    def __init__(self,v, left = None, right = None):

        self.v = v
        self.left = left
        self.right = right

    def get_value(self):
        return self.v




class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {}
        self.head = None
        self.tail = None


    def get(self, key: int) -> int:

        if key not in self.dic:
            return -1

        p = self.dic[key]
        val = p.get_value()

        if self.capacity > 1:
            if p == self.head:
                self.head = p.next
                self.head.left = None
                self.tail.right = p
                p.left = self.tail
                p.right= None
                self.tail = p
            elif p!= self.tail:
                p.left.right = p.right
                p.right.left = p.left
                self.tail.right = p
                p.left = self.tail
                p.right = None
                self.tail = p

        return val


    def put(self, key: int, value: int) -> None:

        new_node = DNode(value)
        self.dic[key] = new_node

        if len(self.dic) == 1:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.right = new_node
            new_node.left = self.tail
            self.tail = new_node

        if len(self.dic) > self.capacity:
            self.head = self.head.right
            self.head.left = None


