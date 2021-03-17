# -*- coding: utf-8 -*-
# @Time    : 2021-03-14 20:18
# @Author  : zxl
# @FileName: 310.py

#TODO 超时


class Solution(object):


    def minHeight(self,s,n,dic):

        Q = []
        visited = [0 for i in range(n)]
        Q.append(s)
        visited[s] = 1


        while len(Q) > 0:
            v = Q.pop(0)
            neighbors = dic[v] if v in dic else []
            for neighbor in neighbors:
                if visited[neighbor] == 0:
                    visited[neighbor] = visited[v] + 1
                    Q.append(neighbor)
        return max(visited) - 1


    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """


        dic = {}
        for edge in edges:
            n1 = edge[0]
            n2 = edge[1]
            if n1 not in dic:
                dic[n1] = []
            if n2 not in dic:
                dic[n2] = []
            dic[n1].append(n2)
            dic[n2].append(n1)

        min_h = n-1
        ans = []
        for i in range(n):
            h = self.minHeight(i,n,dic)
            if h < min_h:
                ans = [i]
                min_h = h
            elif h == min_h:
                ans.append(i)


        return ans


obj = Solution()
n = 2
edges = [[0,1]]
ans = obj.findMinHeightTrees(n,edges)
print(ans)