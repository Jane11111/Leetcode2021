# -*- coding: utf-8 -*-
# @Time    : 2021-03-12 14:32
# @Author  : zxl
# @FileName: 107.py


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        ans = []
        stack = []
        if root:
            stack.append(root)
        while len(stack) != 0:
            l = len(stack)
            cur_layer = []
            for i in range(l):
                p = stack.pop(0)
                cur_layer.append(p.val)
                if p.left:
                    stack.append(p.left)
                if p.right:
                    stack.append(p.right)
            ans.insert(0,cur_layer)
        return ans


obj = Solution()
head = TreeNode(3)
head.left = TreeNode(9)
head.right = TreeNode(20)
head.right.left = TreeNode(15)
head.right.right = TreeNode(7)
ans = obj.levelOrderBottom(head)
print(ans)