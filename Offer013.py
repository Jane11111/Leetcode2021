# -*- coding: utf-8 -*-
# @Time    : 2021-04-23 10:39
# @Author  : zxl
# @FileName: Offer013.py

class Solution:

    def getValidNeighbors(self,i,j,m,n):

        lst = []
        if j+1<n:
            lst.append([i,j+1])
        if j-1>=0:
            lst.append([i,j-1])
        if i-1>=0:
            lst.append([i-1,j])
        if i+1<m:
            lst.append([i+1,j])
        return lst

    def movingCount(self, m: int, n: int, k: int) -> int:

        visited = []
        for i in range(m):
            visited.append([0 for j in range(n)])

        count = 0
        lst = [[0,0]]
        visited[0][0] = -1

        while len(lst)!= 0:
            i,j = lst.pop(0)
            count +=1
            for x,y in self.getValidNeighbors(i,j,m,n):
                if visited[x][y] == -1:
                    continue
                visited[x][y] = -1
                tmp = x
                num = 0
                while tmp:
                    num+=tmp%10
                    tmp //=10
                tmp = y
                while tmp:
                    num+=tmp%10
                    tmp//=10
                if num<=k:
                    lst.append([x,y])
        return count












