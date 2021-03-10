# -*- coding: utf-8 -*-
# @Time    : 2021-03-08 22:12
# @Author  : zxl
# @FileName: 144_2.py


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):


    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        res = []

        if root == None:
            return res

        lst = []
        res.append(root.val)
        lst.append(root)
        while len(lst) > 0:
            p = lst[0]
            if p.left:
                res.append(p.left.val)
                lst.insert(0,p.left)
                p.left = None
            elif p.right:
                lst.pop(0)
                res.append(p.right.val)
                lst.insert(0,p.right)
            else:
                lst.pop(0)
        return res
