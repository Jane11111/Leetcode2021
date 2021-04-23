# -*- coding: utf-8 -*-
# @Time    : 2021-04-22 12:46
# @Author  : zxl
# @FileName: 230_2.py


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:

    def inorder(self,p,lst):
        if p== None:
            return
        self.inorder(p.left,lst)
        lst.append(p.val)
        self.inorder(p.right,lst)



    def kthSmallest(self, root: TreeNode, k: int) -> int:

        ans = []
        self.inorder(root,ans)
        return ans[k]