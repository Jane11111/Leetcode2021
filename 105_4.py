# -*- coding: utf-8 -*-
# @Time    : 2021-05-12 11:50
# @Author  : zxl
# @FileName: 105_4.py


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

            if lst[-1].val!=inorder[j]:

                lst[-1].left = p
                lst.append(p)
            else:

                while len(lst)>1 and inorder[j+1] == lst[-2].val:
                    j+=1
                    lst.pop()
                j+=1

                lst[-1].right = p
                lst.pop()
                lst.append(p)
        return head



