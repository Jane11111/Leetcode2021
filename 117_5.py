# -*- coding: utf-8 -*-
# @Time    : 2021-07-28 11:54
# @Author  : zxl
# @FileName: 117_5.py




class Solution:

    def getNext(self,p):
        if not p:
            return p
        if p.left:
            return p.left
        if p.right:
            return p.right
        return self.getNext(p.next)

    def recConnect(self,root,next): #next及其next的所有子树都已经串好
                                    #现在串root及其子树
        if not root:
            return

        root.next = next

        if root.right:
            self.recConnect(root.right,self.getNext(root.next))
            self.recConnect(root.left,root.right)
        else:
            self.recConnect(root.left,self.getNext(root.next))

    def connect(self, root):

        self.recConnect(root,None)
        return root