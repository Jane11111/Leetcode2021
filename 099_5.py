# -*- coding: utf-8 -*-
# @Time    : 2021-08-04 16:40
# @Author  : zxl
# @FileName: 099_5.py




# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        p1 = None
        p2 = None
        p3 = None
        p4 = None
        last = None

        p = root
        st = []

        while p:
            st.append(p)
            p = p.left

        while len(st)>0:
            p = st.pop()

            if last and last.val>p.val:
                if not p1:
                    p1 = last
                    p2 = p
                else:
                    p3 = last
                    p4 = p
            last = p
            p = p.right
            while p:
                st.append(p)
                p = p.left
        if p3:
            p1.val,p4.val = p4.val, p1.val
        else:
            p1.val,p2.val = p2.val,p1.val






