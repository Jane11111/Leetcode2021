# -*- coding: utf-8 -*-
# @Time    : 2021-03-06 13:44
# @Author  : zxl
# @FileName: 538_2.py


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):

    def __init__(self):
        self.num  = 0

    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        if not root:
            return root
        tmp = root.val

        self.convertBST(root.right)

        root.val = self.num + root.val

        self.num += tmp

        self.convertBST(root.left)



        return root