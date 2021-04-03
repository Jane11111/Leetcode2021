# -*- coding: utf-8 -*-
# @Time    : 2021-03-31 12:58
# @Author  : zxl
# @FileName: 802_2.py


class Solution(object):

    def dfs(self,graph,visited,u):

        visited[u] = self.t

        for neighbor in graph[u]:
            if visited[neighbor] == -1:
                self.t+=1
                self.dfs(graph,visited,neighbor)


        self.t+=1
        visited[u] = self.t
        return





    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """

        self.t = 1

        n = len(graph)
        visited = [-1 for i in range(n)]

        for i in range(n):
            if visited[i] == -1:
                self.dfs(graph,visited,i)

        sorted_idx = sorted(range(n),key = lambda k: visited[k])

        res = []
        for idx in sorted_idx:
            f = True
            for v in graph[idx]:
                if v not in res:
                    f = False
                    break
            if f:
                res.append(idx)
        res.sort()
        return res


obj = Solution()
graph = [[1,2],[2,3],[5],[0],[5],[],[]]
ans = obj.eventualSafeNodes(graph)
print(ans)