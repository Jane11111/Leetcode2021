# -*- coding: utf-8 -*-
# @Time    : 2021-03-14 22:58
# @Author  : zxl
# @FileName: 337.py

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):

    def getMax(self,root,father_robed,dic):

        if not root:
            return 0
        if root in dic and father_robed in dic[root]:
            return dic[root][father_robed]


        if father_robed:
            m1 = self.getMax(root.left,False,dic)
            m2 = self.getMax(root.right,False,dic)
            ans = m1+m2
        else:

            m1 = root.val + self.getMax(root.left,True,dic) + self.getMax(root.right,True,dic)
            m2 = self.getMax(root.left,False,dic) + self.getMax(root.right,False,dic)
            ans = max(m1,m2)
        dic[root] = {}
        dic[root][father_robed] = ans
        return ans



    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        ans = self.getMax(root,False,{})
        return ans



