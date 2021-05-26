# -*- coding: utf-8 -*-
# @Time    : 2021-05-25 11:53
# @Author  : zxl
# @FileName: 129_5.py



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:


    def sumNumbers(self, root: TreeNode) -> int:

        ans = 0

        st1 = [root] if root else []
        st2 = [0] if root else []

        while len(st1)>0:

            p = st1.pop(0)
            num = st2.pop(0)

            if not p.left and not p.right:
                ans+=(num+p.val)
            if p.left:
                st1.append(p.left)
                st2.append((num+p.val)*10)
            if p.right:
                st1.append(p.right)
                st2.append((num+p.val)*10)
        return ans
