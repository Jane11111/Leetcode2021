# -*- coding: utf-8 -*-
# @Time    : 2021-03-06 22:03
# @Author  : zxl
# @FileName: 938.py


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        if root == None:
            return 0

        res = 0

        if root.val < low:
            res += self.rangeSumBST(root.right,low,high)
        elif root.val > high:
            res += self.rangeSumBST(root.left,low,high)
        else:
            res += (self.rangeSumBST(root.right,low,high) + self.rangeSumBST(root.left,low,high)) +root.val
        return res