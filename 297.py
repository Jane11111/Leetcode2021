# -*- coding: utf-8 -*-
# @Time    : 2021-05-15 17:39
# @Author  : zxl
# @FileName: 297.py


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

        Q = [root] if root else []
        lst = []

        while len(Q)>0:
            l = len(Q)
            f = False
            while l:
                l-=1
                p = Q.pop(0)
                if p:
                    lst.append(p.val) # 每次pop的时候，都要把v或者None放到lst里面
                    Q.append(p.left) # Q中存储上一层node的全部子孙（包括None）
                    Q.append(p.right)
                    if p.left or p.right:
                        f = True
                else:
                    lst.append(None)
            if not f:
                break
        s = ''
        for v in lst:
            if v!=None:
                s+=str(v)
            else:
                s+='null'
            s+=','
        if len(s)>0:
            s = s[:-1]
        if s[-4:] == 'null':
            s = s[:-5]
        return s



    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        if len(data) == 0:
            return None

        arr = data.split(',')

        root = TreeNode(int(arr[0]))
        p_lst = [root] # 放上一层全部node，不包括None，那么对应的arr中一定包括这部分的全部子孙（但是最后一层可能提前断掉）

        j = 1
        while j<len(arr):

            l = len(p_lst)
            while l and j <len(arr): # 最后一层，会删掉上一层没有子孙的node，（该node后面的node全都没有子孙）
                l-=1
                p = p_lst.pop(0)

                left = arr[j]

                if left != 'null':
                    p.left = TreeNode(int(left))
                    p_lst.append(p.left)
                if j+1 == len(arr): # 上一层最后一个节点没有右节点
                    j+=1
                    break
                right = arr[j + 1]
                if right != 'null':
                    p.right = TreeNode(int(right))
                    p_lst.append(p.right)
                j+=2


        return root

