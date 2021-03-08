# -*- coding: utf-8 -*-
# @Time    : 2021-03-05 22:45
# @Author  : zxl
# @FileName: 199.py

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right




class Solution(object):


    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        res = []
        if root == None:
            return res
        res.append(root.val)
        l_res = self.rightSideView(root.left)
        r_res = self.rightSideView(root.right)

        res.extend(r_res)

        for i in range(len(r_res),len(l_res),1):
            res.append(l_res[i])
        return res


