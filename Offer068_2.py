# -*- coding: utf-8 -*-
# @Time    : 2021-06-22 14:40
# @Author  : zxl
# @FileName: Offer068_2.py


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def formDic(self,p,root,dic):

        if root == None:
            return

        dic[root] = p
        self.formDic(root,root.left,dic)
        self.formDic(root,root.right,dic)

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':


        dic = {}
        self.formDic(None,root,dic)
        lst1 = [-1,p]
        while dic[p] != None:
            lst1.append(dic[p])
            p = dic[p]

        lst2 = [-2,q]
        while dic[q] != None:
            lst2.append(dic[q])
            q = dic[q]

        i = -1
        while lst1[i]==lst2[i]:
            i-=1

        return lst1[i+1]

