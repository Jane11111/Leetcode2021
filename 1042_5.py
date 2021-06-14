# -*- coding: utf-8 -*-
# @Time    : 2021-06-07 21:09
# @Author  : zxl
# @FileName: 1042_5.py





# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:

    def recClone(self,real_root,visited):
        if real_root == None :
            return

        clone_root = Node(real_root.val)
        visited[real_root.val] = clone_root

        for p in real_root.neighbors:
            if p.val in visited:
                clone_root.neighbors.append(visited[p.val])
            else:
                # clone_p = Node(p.val)
                # clone_root.neighbors.append(clone_p)
                # visited[p.val] = clone_p
                self.recClone(p,visited)
                clone_root.neighbors.append(visited[p.val])
        return

    def cloneGraph(self, node: 'Node') -> 'Node':

        visited = {}
        self.recClone(node,visited)

        if node == None:
            return node
        return visited[node.val]
