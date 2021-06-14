# -*- coding: utf-8 -*-
# @Time    : 2021-06-14 17:22
# @Author  : zxl
# @FileName: Offer037_3.py


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
        if root == None:
            return ''
        l = self.serialize(root.left)
        r = self.serialize(root.right)

        s = str(root.val)
        s = s+'('+str(len(l))+')'+l+r
        return s




    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        if len(data) == 0:
            return None

        i = 0
        while data[i]!= '(':
            i+=1

        j = i+1
        while data[j]!=')':
            j+=1

        v = int(data[:i])
        left_len = int(data[i+1:j])

        root = TreeNode(v)
        root.left = self.deserialize(data[j+1:j+1+left_len])
        root.right = self.deserialize(data[j+left_len+1:])
        return root
