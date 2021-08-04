# -*- coding: utf-8 -*-
# @Time    : 2021-08-02 15:56
# @Author  : zxl
# @FileName: 146_3.py


class DNode():

    def __init__ (self,key,val,left=None,right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right



class LRUCache:

    def __init__(self, capacity: int):

        self.head = DNode(-1,-1)
        self.tail = DNode(-1,-1)
        self.head.right = self.tail
        self.tail.left = self.head

        self.count = 0
        self.capacity = capacity
        self.dic = {}


    def get(self, key: int) -> int:

        if key not in self.dic or not self.dic[key]:
            return -1

        p = self.dic[key]
        self.update(p)
        return p.val

    def update(self,p):
        p.left.right = p.right
        p.right.left = p.left

        p.right = self.head.right
        p.left = self.head
        p.right.left = p
        p.left.right = p

    def put(self, key: int, value: int) -> None:


        if key not in self.dic or not self.dic[key]:

            p = DNode(key,value)

            self.dic[key] = p

            self.count+=1

            p.left = self.head
            p.right = self.head.right

            p.left.right = p
            p.right.left = p

        else:
            p = self.dic[key]
            p.val = value
            self.update(p) #更新它的位置

        if self.count>self.capacity:
            p = self.tail.left
            self.tail.left = p.left
            p.left.right = self.tail

            key = p.key
            self.dic[key] = None
            self.count-=1







