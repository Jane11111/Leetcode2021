# -*- coding: utf-8 -*-
# @Time    : 2021-06-10 11:14
# @Author  : zxl
# @FileName: 685.py


class Solution:




    def find(self,arr,idx):
        if arr[idx] == idx:
            return idx
        arr[idx] = self.find(arr,arr[idx])
        return arr[idx]

    def union(self,arr,idx1,idx2):
        arr[idx2] = self.find(arr,idx1)

    def init(self,n):
        arr = [i for i in range(n+1)]
        return arr
    def containsLoop(self,edges, deleted_idx):

        arr = self.init(len(edges))
        for i in range(len(edges)):
            if i == deleted_idx:
                continue
            x,y = edges[i]

            p1 = self.find(arr,x)
            if p1 == y:
                return True
            self.union(arr,x,y)
        return False


    def findRedundantDirectedConnection(self, edges ) :

        n = len(edges)
        indegree = {i :0 for i in range(n+1)}

        node_id = -1
        for x,y in edges:
            indegree[y] +=1
            if indegree[y] == 2:
                node_id = y

        if node_id != -1: # 可能有环，也可能没有环，只要保证删了以后没有环就行
            # 如果加了边，也没有环，那么删除哪条都可以
            # 如果加了边，形成了环，那么必须删除那条产生了环的边
            # 换句话说，只要删除后，没有环就行了

            for i in range(n-1,-1,-1):
                if edges[i][1]!=node_id:
                    continue
                f = self.containsLoop(edges,i)
                if not f:
                    return edges[i]

        else: # 出现了环路
            arr = self.init(n)
            for x,y in edges:
                p1 = self.find(arr,x)
                if p1 == y:
                    return [x,y]
                self.union(arr,x,y)













