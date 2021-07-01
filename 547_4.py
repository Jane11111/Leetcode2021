# -*- coding: utf-8 -*-
# @Time    : 2021-07-01 11:59
# @Author  : zxl
# @FileName: 547_4.py





class Solution:

    def find(self,arr,i,rank):
        if arr[i] == i:
            return i
        arr[i] = self.find(arr,arr[i],rank) # 路径压缩
        rank[i] = 2 # 同时要改变秩
        return arr[i]

    def merge(self,i,j,arr,rank):



        x = self.find(arr,i,rank)
        y = self.find(arr,j,rank)

        if x == y :
            return

        if x<=y:
            arr[x] = y
        else:
            arr[y] = x

        if x == y:
            rank[y]+=1




    def findCircleNum(self, isConnected) -> int:

        n = len(isConnected)
        arr = [i for i in range(n)]
        rank = [1 for i in range(n)]

        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    self.merge(i,j,arr,rank)

        sets = set([])
        for i in range(n):
            sets.add(self.find(arr,i,rank))
        return len(sets)



