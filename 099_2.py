# -*- coding: utf-8 -*-
# @Time    : 2021-06-11 16:12
# @Author  : zxl
# @FileName: 099_2.py




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

        p = root
        st = []
        prev = None
        x = None
        y = None

        while len(st)>0 or p:

            while p:
                st.append(p)
                p = p.left

            p = st.pop()
            if prev and prev.val>p.val:
                y = p
                if not x:
                    x = prev

            prev = p
            p = p.right
        x.val,y.val = y.val,x.val






obj = Solution()
p1 = TreeNode(1)
p2 = TreeNode(2)
p3 = TreeNode(3)
p4 = TreeNode(4)
p2.left = p4
p2.right = p1
p1.left = p3
obj.recoverTree(p2)