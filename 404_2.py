# -*- coding: utf-8 -*-
# @Time    : 2021-06-24 21:35
# @Author  : zxl
# @FileName: 404_2.py


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def sumOfLeftLeaves(self, root: TreeNode) -> int:

        if not root or (not root.left and not root.right):
            return 0

        ans = 0

        lst = [root] if root else []

        while len(lst)>0:

            p = lst.pop(0)

            if p.left:
                if not p.left.left and not p.left.right:
                    ans+=p.left.val
                else:
                    lst.append(p.left)
            if p.right:
                if not p.right.left and not p.right.right:
                    pass
                else:
                    lst.append(p.right)
        return ans


