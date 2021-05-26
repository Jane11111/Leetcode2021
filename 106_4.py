# -*- coding: utf-8 -*-
# @Time    : 2021-05-12 15:27
# @Author  : zxl
# @FileName: 106_4.py


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



# 对于postorder 而言，i-1要么是i的right，要么是某个节点的left
# 至于说是哪个节点的left，需要根据inorder来判断，从inorder里面找到第一个有left节点的node（如果没有left，那么inorder的正序=postorder的倒序）
class Solution:

    def buildTree(self, inorder, postorder) -> TreeNode:


        if len(inorder) == 0:
            return None

        root = TreeNode(postorder[-1])

        lst = [root]
        j = len(inorder)-1

        for i in range(len(postorder)-1,-1,-1):

            p = TreeNode(postorder[i])

            if lst[-1].val != inorder[j]:
                lst[-1].right = p
                lst.append(p)
            else:
                while len(lst)>0 and lst[-1].val == inorder[j]:
                    j-=1
                    cur_root = lst.pop()

                cur_root.left = p
                lst.append(p)
        return root


