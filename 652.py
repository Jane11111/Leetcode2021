# -*- coding: utf-8 -*-
# @Time    : 2021-08-20 21:43
# @Author  : zxl
# @FileName: 652.py



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def recFind(self,root,node_dic,id_dic):
        if root in node_dic:
            return node_dic[root]

        if root == None:
            return 'None'
        left_id = self.recFind(root.left,node_dic,id_dic)
        right_id = self.recFind(root.right,node_dic,id_dic)

        cur_id = '('+left_id+'),'+str(root.val)+',('+right_id+')'

        node_dic[root] = cur_id
        if cur_id not in id_dic:
            id_dic[cur_id] = []
        id_dic[cur_id].append(root)
        return cur_id

    def findDuplicateSubtrees(self, root: TreeNode) :

        node_dic = {}
        id_dic = {}
        self.recFind(root,node_dic,id_dic)

        ans = []
        for id_val in id_dic:
            if len(id_dic[id_val])>1:
                ans.append(id_dic[id_val][0])
        return ans

