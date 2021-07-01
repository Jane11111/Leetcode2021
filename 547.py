# -*- coding: utf-8 -*-
# @Time    : 2021-07-01 11:27
# @Author  : zxl
# @FileName: 547.py


class Solution:


    def dfs(self,cur,n,isConnected,visited):
        visited[cur] = True

        for i in range(n):
            if isConnected[cur][i] and not visited[i]:
                self.dfs(i,n,isConnected,visited)



    def findCircleNum(self, isConnected ) -> int:

        n = len(isConnected)
        visited = {i:False for i in range(n)}
        count = 0
        for i in range(n):
            if not visited[i]:
                count += 1
                self.dfs(i,n,isConnected,visited)
        return count





