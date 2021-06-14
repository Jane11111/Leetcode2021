# -*- coding: utf-8 -*-
# @Time    : 2021-06-14 16:52
# @Author  : zxl
# @FileName: Offer037_2.py


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

        p_lst = [root] if root else []
        lst = [root.val] if root else []
        while len(p_lst)>0:
            l = len(p_lst)
            while l:
                l-=1
                p = p_lst.pop(0)
                if p.left:
                    p_lst.append(p.left)
                    lst.append(p.left.val)
                else:
                    lst.append(None)
                if p.right:
                    p_lst.append(p.right)
                    lst.append(p.right.val)
                else:
                    lst.append(None)
        return str(lst)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        lst = eval(data)
        print(lst)

        if len(lst) == 0:
            return None

        p = TreeNode(lst[0])
        root = p
        last_layer = [p]
        s = 1
        while s<len(lst) :
            l = len(last_layer)
            while l:
                p = last_layer.pop(0)
                l-=1

                lc = lst[s]
                rc = lst[s+1]
                s+=2

                if lc!= None:
                    p.left = TreeNode(lc)
                    last_layer.append(p.left)
                if rc!=None:
                    p.right = TreeNode(rc)
                    last_layer.append(p.right)
        return root




