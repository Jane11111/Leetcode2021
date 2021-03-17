# -*- coding: utf-8 -*-
# @Time    : 2021-03-12 15:42
# @Author  : zxl
# @FileName: 116_2.py


# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution(object):

    def recursiveConstruct(self,root,next):

        if root == None :
            return
        root.next = next
        self.recursiveConstruct(root.left,root.right)
        self.recursiveConstruct(root.right,next if not next else next.left)


    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        self.recursiveConstruct(root,None)
        return root
