# -*- coding: utf-8 -*-
# @Time    : 2021-06-07 20:52
# @Author  : zxl
# @FileName: 1042_4.py




# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':


        if node == None:
            return None

        dic = {node.val: Node(node.val)}

        st = [node]
        visited = {}
        visited[node.val] = True

        while len(st)>0:

            p = st.pop(0)

            for n_node in p.neighbors:

                if n_node.val not in dic:
                    dic[n_node.val] = Node(n_node.val)
                dic[p.val].neighbors.append(dic[n_node.val])
                # dic[n_node.val].neighbors.append(dic[p.val])
                if n_node.val not in  visited :
                    st.append(n_node)
                    visited[n_node.val] = True
        return dic[node.val]


