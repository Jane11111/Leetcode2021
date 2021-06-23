# -*- coding: utf-8 -*-
# @Time    : 2021-06-22 10:27
# @Author  : zxl
# @FileName: 105_7.py


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def buildTree(self, preorder, inorder) -> TreeNode:


        root = TreeNode(preorder[0])
        i =1
        idx = 0
        st = [root]
        while i<len(preorder):

            while st[-1].val!=inorder[idx]: # 走到最左边
                p = TreeNode(preorder[i])
                st[-1].left = p
                st.append(p)
                i+=1

            if i>=len(preorder):
                break

            while len(st)>0 and st[-1].val == inorder[idx]:
                p = st.pop()
                idx+=1
            p.right = TreeNode(preorder[i])
            i+=1
            st.append(p.right)
        return root


