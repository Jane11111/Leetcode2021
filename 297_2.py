# -*- coding: utf-8 -*-
# @Time    : 2021-05-15 18:46
# @Author  : zxl
# @FileName: 297_2.py




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
        s = str(root.val)
        l = self.serialize(root.left)
        r = self.serialize(root.right)
        s = s+'('+str(len(l))+')'
        s = s+l+r
        return s






    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        if len(data)==0:
            return None

        i = 0
        while data[i]!='(':
            i+=1
        v = int(data[:i])
        j=i
        while data[j]!=')':
            j+=1
        length = int(data[i+1:j])
        l = data[j+1:j+1+length]
        r = data[j+1+length:]

        root = TreeNode(v)

        root.left = self.deserialize(l)
        root.right = self.deserialize(r)
        return root


