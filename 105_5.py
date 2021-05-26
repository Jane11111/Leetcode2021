# -*- coding: utf-8 -*-
# @Time    : 2021-05-12 14:58
# @Author  : zxl
# @FileName: 105_5.py



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder , inorder ) -> TreeNode:

        if len(preorder) == 0:
            return None

        head = TreeNode(preorder[0])
        lst = [head]

        j = 0

        for i in range(1,len(preorder)):

            p = TreeNode(preorder[i])

            if lst[-1].val != inorder[j]:
                lst[-1].left = p
                lst.append(p)
            else:
                while len(lst)>0 and lst[-1].val == inorder[j]:
                    j+=1
                    cur_root = lst.pop()
                cur_root.right = p
                lst.append(p)
        return head


