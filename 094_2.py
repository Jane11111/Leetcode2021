# -*- coding: utf-8 -*-
# @Time    : 2021-03-08 21:37
# @Author  : zxl
# @FileName: 094_2.py


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        res = []
        if root == None:
            return res

        s = [root]
        while len(s) >0:
            p = s[0]
            if p.left:
                s.insert(0,p.left)
                p.left = None
            else:
                s.pop(0)
                res.append(p.val)
                if p.right:
                    s.insert(0,p.right)
        return res



root = TreeNode(1)
root.right = TreeNode(2)
root.right.left=TreeNode(3)

obj = Solution()
lst = obj.inorderTraversal(root)
print(lst)