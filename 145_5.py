# -*- coding: utf-8 -*-
# @Time    : 2021-05-31 16:40
# @Author  : zxl
# @FileName: 145_5.py



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode):


        lst = []
        st = []

        p = root
        while p:
            st.append(p)
            lst.insert(0,p.val)
            p = p.right

        while len(st)>0:
            p = st.pop()

            p = p.left
            while p:
                st.append(p)
                lst.insert(0,p.val)
                p = p.right
        return lst



