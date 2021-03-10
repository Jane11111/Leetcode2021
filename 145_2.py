# -*- coding: utf-8 -*-
# @Time    : 2021-03-08 22:40
# @Author  : zxl
# @FileName: 145_2.py


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):



    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []

        if root == None:
            return res

        lst = [root]

        while len(lst) != 0:
            p = lst[0]
            if p.left == None and  p.right == None:
                res.append(p.val)
                lst.pop(0)
                continue
            if p.right:
                lst.insert(0,p.right)
                p.right = None
            if p.left:
                lst.insert(0,p.left)
                p.left = None

        return res


