# -*- coding: utf-8 -*-
# @Time    : 2021-05-18 17:34
# @Author  : zxl
# @FileName: 124_2.py



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def recFind(self,root):

        if root == None:
            return float('-inf'),float('-inf')
        l_max1,l_max2 = self.recFind(root.left)
        r_max1,r_max2 = self.recFind(root.right)

        cur_max1 = max(l_max1+root.val,r_max1+root.val,root.val) #以当前node开始的最大value
        cur_max2 = max(l_max2,r_max2,  l_max1+r_max1+root.val,cur_max1) #以当前node为root的树所能形成的最长的路径
        return cur_max1,cur_max2



    def maxPathSum(self, root: TreeNode) -> int:

        v1, v2 = self.recFind(root)
        return v2




