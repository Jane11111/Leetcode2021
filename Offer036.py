# -*- coding: utf-8 -*-
# @Time    : 2021-04-23 14:24
# @Author  : zxl
# @FileName: Offer036.py




# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:


    def solve(self,root):
        if root.left == None and root.right == None:
            return root,root

        if root.left:
            lh,lt = self.solve(root.left)
        else:
            lh,lt = root,root
        if root.right:
            rh,rt = self.solve(root.right)
        else:
            rh,rt = root,root
        if root.left:
            root.left= lt
            lt.right = root

        if root.right:
            root.right = rh
            rh.left = root


        return lh,rt

    def treeToDoublyList(self, root: 'Node') -> 'Node':

        if root == None:
            return root

        h,t = self.solve(root)
        if h:
            h.left = t
        if t:
            t.right = h
        return h

p = Node(2)
p.left = Node(1)
obj = Solution()
h = obj.treeToDoublyList(p)
print(h.val)




