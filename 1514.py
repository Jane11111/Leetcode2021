# -*- coding: utf-8 -*-
# @Time    : 2021-06-10 21:53
# @Author  : zxl
# @FileName: 1514.py


import  heapq
class Solution:


    def maxProbability(self, n: int, edges , succProb , start: int, end: int) -> float:

        dic = {}
        for i in range(len(edges)):
            x,y = edges[i]
            if x not in dic:
                dic[x] = {}
            if y not in dic:
                dic[y] = {}
            dic[x][y] = succProb[i]
            dic[y][x] = succProb[i]
        dist = [0 for i in range(n)]
        dist[start] = -1

        que = [(-1,start)]

        while len(que)>0:

            p,u = heapq.heappop(que)
            if u == end:
                return -p

            if dist[u] <p or u not in dic:
                continue
            for v in dic[u]:
                p2 = dic[u][v]

                if p*p2<dist[v]:
                    dist[v] = p*p2
                    heapq.heappush(que,(dist[v],v))
        return -dist[end]







