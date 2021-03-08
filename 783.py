# -*- coding: utf-8 -*-
# @Time    : 2021-03-06 16:35
# @Author  : zxl
# @FileName: 783.py


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):


    def recursiveFind(self,root):

        min_val = root.val
        max_val = root.val

        min_diff = 1000000

        if root.left:
            min_val1,max_val1,diff1 = self.recursiveFind(root.left)
            min_val = min(min_val,min_val1) # 注意这里min, max val的寻找应该比较的对象
            max_val = max(max_val,max_val1)
            min_diff = min(root.val-max_val1,diff1)
        if root.right:
            min_val2,max_val2,diff2 = self.recursiveFind(root.right)
            min_val = min(min_val, min_val2)
            max_val = max(max_val, max_val2)

            min_diff = min(min_diff,diff2)
            min_diff = min(min_val2 - root.val, min_diff)

        # if not root.left and not root.right:
        #     min_val = root.val
        #     max_val = root.val
        #     min_diff = 1000000
        return min_val, max_val,min_diff

    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        _,_,res = self.recursiveFind(root)
        return res

