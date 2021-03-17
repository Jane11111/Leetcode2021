# -*- coding: utf-8 -*-
# @Time    : 2021-03-12 14:22
# @Author  : zxl
# @FileName: 103.py



# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        lst = []
        ans = []
        if root:
            lst.append(root)
        r2l = False
        while len(lst) > 0:

            cur_layer = []
            l = len(lst)

            if r2l:
                for i in range(l-1,-1,-1):
                    p = lst.pop(len(lst)-1)
                    cur_layer.append(p.val)
                    if p.right:
                        lst.insert(0,p.right)
                    if p.left:
                        lst.insert(0,p.left)

            else:
                for i in range(l):
                    p = lst.pop(0)
                    cur_layer.append(p.val)
                    if p.left:
                        lst.append(p.left)
                    if p.right:
                        lst.append(p.right)
            r2l = not r2l
            ans.append(cur_layer)
        return ans

obj = Solution()
head = TreeNode(3)
head.left = TreeNode(9)
head.right = TreeNode(20)
head.right.left = TreeNode(15)
head.right.right = TreeNode(7)
ans = obj.zigzagLevelOrder(head)
print(ans)

