# -*- coding: utf-8 -*-
# @Time    : 2021-07-01 11:35
# @Author  : zxl
# @FileName: 547_3.py





class Solution:

    def find(self,arr,i):
        if arr[i] == i:
            return i
        arr[i] = self.find(arr,arr[i]) # 路径压缩
        return arr[i]

    def merge(self,i,j,arr):

        arr[self.find(arr,i)] = self.find(arr,j)




    def findCircleNum(self, isConnected) -> int:

        n = len(isConnected)
        arr = [i for i in range(n)]

        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    self.merge(i,j,arr)

        sets = set([])
        for i in range(n):
            sets.add(self.find(arr,i))
        return len(sets)



