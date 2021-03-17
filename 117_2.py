# -*- coding: utf-8 -*-
# @Time    : 2021-03-12 16:21
# @Author  : zxl
# @FileName: 117_2.py



# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next



class Solution(object):

    def getNext(self,next):
        if not next:
            return None

        if next.left:
            return next.left
        elif next.right:
            return next.right
        else:
            return self.getNext(next.next)

    def recursiveConstruct(self,root,next):

        if not root:
            return

        root.next = next

        if root.right:
            lr = root.right
        else:
            lr =  self.getNext(next)

        self.recursiveConstruct(root.right, self.getNext(next))

        self.recursiveConstruct(root.left,lr)



    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """

        self.recursiveConstruct(root,None)
        return root
