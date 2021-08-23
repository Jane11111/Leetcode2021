# -*- coding: utf-8 -*-
# @Time    : 2021-08-15 11:37
# @Author  : zxl
# @FileName: 787_5.py



import heapq



class Solution:
    def findCheapestPrice(self, n: int, flights, src: int, dst: int, k: int) -> int:

        graph = {}
        for f,t,p in flights:
            if f not in graph:
                graph[f] = {}
            graph[f][t] = p

        # lst = []
        ans = float('inf')
        # heapq.heappush(lst,[0,src,k+1])
        lst = [[0,src,k+1]]
        while len(lst)>0:

            # p,u,step = heapq.heappop(lst)
            p, u, step = lst.pop()
            if u == dst:
                ans = min(ans,p)

            if u not in graph or step == 0:
                continue

            for v in graph[u]:
                # heapq.heappush(lst,[p+graph[u][v],v,step-1])
                lst.append([p+graph[u][v],v,step-1])
        if ans == float('inf'):
            return -1
        return ans



obj = Solution()
n = 4
flights = [[0,1,1],[0,2,5],[1,2,1],[2,3,1]]
src = 0
dst = 3
k = 1
ans = obj.findCheapestPrice(n,flights,src,dst,k)
print(ans)



