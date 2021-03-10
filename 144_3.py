# -*- coding: utf-8 -*-
# @Time    : 2021-03-08 22:22
# @Author  : zxl
# @FileName: 144_3.py


class Solution(object):


    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        res = []
        if root == None:
            return []

        lst = [root]
        while len(lst)!= 0:
            p = lst.pop(0)
            res.append(p.val)
            if p.right:
                lst.insert(0,p.right)
            if p.left:
                lst.insert(0,p.left)
        return res
