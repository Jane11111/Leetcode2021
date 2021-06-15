# -*- coding: utf-8 -*-
# @Time    : 2021-06-15 16:40
# @Author  : zxl
# @FileName: 145_6.py


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode):


        p = root

        st = []
        lst = []
        while p:
            st.append(p)
            lst.insert(0, p.val)
            p = p.right

        while len(st)>0:

            p = st.pop()
            p = p.left
            while p:
                st.append(p)
                lst.insert(0, p.val)
                p = p.right

        return lst
