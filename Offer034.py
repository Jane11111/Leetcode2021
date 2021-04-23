# -*- coding: utf-8 -*-
# @Time    : 2021-04-23 14:05
# @Author  : zxl
# @FileName: Offer034.py



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:



    def pathSum(self, root: TreeNode, target: int)  :

        ans = []

        if root == None:
            return ans
        if root.left == None and root.right == None and root.val == target:
            return [[root.val]]

        left_path = self.pathSum(root.left, target - root.val)
        right_path = self.pathSum(root.right, target - root.val)

        left_path.extend(right_path)
        for i in range(len(left_path)):
            left_path[i].insert(0, root.val)
        return left_path


