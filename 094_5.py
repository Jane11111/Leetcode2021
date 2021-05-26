# -*- coding: utf-8 -*-
# @Time    : 2021-05-12 16:34
# @Author  : zxl
# @FileName: 094_5.py



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def inorderTraversal(self, root: TreeNode):

        if root == None:
            return []

        st = []
        lst = []
        p = root
        while p:
            st.append(p)
            p = p.left
        while len(st)>0:

            p = st.pop()
            lst.append(p.val)

            p = p.right
            while p:
                st.append(p )
                p = p.left
        return lst


