# -*- coding: utf-8 -*-
# @Time    : 2021-06-09 11:14
# @Author  : zxl
# @FileName: 684_2.py




class Solution:

    def find(self,parent,idx):
        if parent[idx] == idx:
            return idx
        parent[idx] = self.find(parent,parent[idx])
        return parent[idx]
    def union(self,parent,idx1,idx2):
        parent[self.find(parent,idx1)] = self.find(parent,idx2)

    def findRedundantConnection(self, edges ) :

        n = len(edges)
        parent = [i for i in range(0,n+1)]

        for x,y in edges:
            if self.find(parent,x) == self.find(parent,y):
                return [x,y]
            else:
                self.union(parent,x,y)


