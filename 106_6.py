# -*- coding: utf-8 -*-
# @Time    : 2021-06-22 11:43
# @Author  : zxl
# @FileName: 106_6.py





# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder , postorder ) -> TreeNode:

        if len(inorder) == 0:
            return None
        root = TreeNode(postorder[-1])

        st = [root]
        i = len(postorder)-2
        idx = len(inorder)-1
        while i>=0:

            while st[-1].val!=inorder[idx]:
                p = TreeNode(postorder[i])
                i-=1
                st[-1].right = p
                st.append(p)

            if i<0:
                break

            while len(st)>0 and st[-1].val == inorder[idx]:
                p = st.pop()
                idx-=1

            p.left = TreeNode(postorder[i])
            i-=1
            st.append(p.left)
        return root


