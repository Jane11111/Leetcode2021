# -*- coding: utf-8 -*-
# @Time    : 2021-03-13 21:49
# @Author  : zxl
# @FileName: 133.py


# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """

        if node == None:
            return None

        Q1 = []
        Q2 = []
        new_node = Node(node.val)
        # for neighbor in node.neighbors:
        #     new_neighbor = Node(neighbor.val,[new_node])
        #     new_node.neighbors.append(new_neighbor)
        node.val = -1
        Q1.append(node)
        Q2.append(new_node)
        while len(Q1) > 0:
            node1 = Q1.pop(0)
            node2 = Q2.pop(0)
            for neighbor in node1.neighbors:
                if neighbor.val > 0:
                    new_neighbor = Node(neighbor.val,[node2])
                    node2.neighbors.append(new_neighbor)
                    neighbor.val = -1
                    Q1.append(neighbor)
                    Q2.append(new_neighbor)
        return new_node


node = Node(1)
node.neighbors.append(Node(2))
node.neighbors.append(Node(3))

obj = Solution()
new_node = obj.cloneGraph(node)
print(new_node)








