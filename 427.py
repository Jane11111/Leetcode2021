# -*- coding: utf-8 -*-
# @Time    : 2021-06-25 15:36
# @Author  : zxl
# @FileName: 427.py



# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

import numpy as np
class Solution:
    def construct(self, grid ) -> 'Node':

        grid = np.array(grid)
        n = len(grid)

        f = False # 是否有不同值
        v = grid[0][0]
        for i in range(n):
            for j in range(n):
                if grid[i][j] != v:
                    f = True
                    break

        if not f:
            root = Node(grid[0][0],1,None,None,None,None)
            return root


        topleft = self.construct(grid[0:n//2,0:n//2])
        topright = self.construct(grid[0:n//2,n//2:])
        bottomleft = self.construct(grid[n//2:,0:n//2])
        bottomright = self.construct(grid[n//2:,n//2:])

        root = Node(1, 0, topleft, topright, bottomleft, bottomright)
        return root




