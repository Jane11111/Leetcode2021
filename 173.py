# -*- coding: utf-8 -*-
# @Time    : 2021-04-13 21:59
# @Author  : zxl
# @FileName: 173.py


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.lst = []
        p = root
        while p:
            self.lst.append(p)
            p = p.left


    def next(self) -> int:
        p = self.lst.pop()
        v = p.val
        p = p.right
        while p:
            self.lst.append(p)
            p = p.left
        return v


    def hasNext(self) -> bool:
        return len(self.lst)>0



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
