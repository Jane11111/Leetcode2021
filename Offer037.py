# -*- coding: utf-8 -*-
# @Time    : 2021-04-23 14:50
# @Author  : zxl
# @FileName: Offer037.py


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        lst = []
        Q = [root] if root else []

        while len(Q) >0:
            p = Q.pop()
            if not p:
                lst.append(None)
                continue
            Q.append(p.left)
            Q.append(p.right)
        while len(lst)>0 and lst[-1] == None:
            lst.pop()
        return str(lst)


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = data[1:-1]
        if len(data) == 0:
            return None
        lst = data.split(',')


        head = TreeNode(int(data[0]))
        Q = [head]
        i = 1
        while i<len(lst):
            p = Q.pop()
            left = lst[i]
            if left != 'null':
                p.left = TreeNode(int(left))
                Q.append(p.left)
            if i+1<len(lst):
                right = lst[i+1]
                if right != 'null':
                    p.right = TreeNode(int(right))
                    Q.append(p.right)
            i+=1
        return head


