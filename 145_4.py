# -*- coding: utf-8 -*-
# @Time    : 2021-05-12 16:44
# @Author  : zxl
# @FileName: 145_4.py




# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) :


        if root == None:
            return []

        st = []
        lst = []
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


