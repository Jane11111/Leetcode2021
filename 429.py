# -*- coding: utf-8 -*-
# @Time    : 2021-06-25 15:53
# @Author  : zxl
# @FileName: 429.py



# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') :

        lst = [root] if root else []
        ans = []
        while len(lst)>0:

            l = len(lst)
            cur_nodes = []
            while l:
                l-=1
                p = lst.pop(0)
                cur_nodes.append(p.val)
                for cp in p.children:
                    if cp:
                        lst.append(cp)
            ans.append(cur_nodes)
        return ans