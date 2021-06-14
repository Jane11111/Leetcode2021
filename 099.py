# -*- coding: utf-8 -*-
# @Time    : 2021-04-27 12:44
# @Author  : zxl
# @FileName: 099.py


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:


    def inorder(self,root,lst):

        if root == None:
            return

        self.inorder(root.left,lst)
        lst.append(root)
        self.inorder(root.right,lst)



    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        lst = []

        self.inorder(root,lst)

        arr = [False for i in range(len(lst))]

        max_val = lst[0].val
        for i in range(1,len(lst)):
            if max_val > lst[i].val:
                arr[i] = True
            max_val = max(max_val,lst[i].val)
        min_val = lst[-1].val
        for i in range(len(lst)-2,-1,-1):
            if min_val<lst[i].val:
                arr[i] = True
            min_val = min(min_val,lst[i].val)

        p1 = -1
        p2 = -1
        for i in range(len(lst)):
            if arr[i] == True:
                if p1== -1:
                    p1 = i
                else:
                    p2 = i
        lst[p1].val, lst[p2].val = lst[p2].val,lst[p1].val




obj = Solution()
p1 = TreeNode(1)
p2 = TreeNode(2)
p3 = TreeNode(3)
p4 = TreeNode(4)
p2.left = p4
p2.right = p1
p1.left = p3
obj.recoverTree(p2)
