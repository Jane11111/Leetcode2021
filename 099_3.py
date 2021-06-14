# -*- coding: utf-8 -*-
# @Time    : 2021-06-11 17:03
# @Author  : zxl
# @FileName: 099_3.py




# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:


    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        p = root
        prev = None
        x = None
        y = None

        while p:
            tmp = p
            if not p.left:

                if prev and prev.val > p.val:
                    y = p
                    if not x:
                        x = prev

                prev = p # prev放的是已经访问过的最右边的节点
                p = p.right

            else:
                p = p.left
                while p.right and p.right!=tmp:
                    p = p.right

                if p.right == None:


                    p.right = tmp

                    p = tmp.left
                else:

                    prev = p
                    p = tmp
                    if prev and prev.val > p.val:
                        y = p
                        if not x:
                            x = prev

                    prev.right = None # 断开链接
                    prev = tmp # prev放的是已经访问过的最右边的节点
                    p = tmp.right


        x.val,y.val = y.val,x.val



obj = Solution()
p1 = TreeNode(1)
p2 = TreeNode(2)
p3 = TreeNode(3)
p4 = TreeNode(4)
p2.left = p4
p2.right = p1
p1.left = p3
obj.recoverTree(p2)