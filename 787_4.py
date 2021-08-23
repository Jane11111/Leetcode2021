# -*- coding: utf-8 -*-
# @Time    : 2021-08-15 11:23
# @Author  : zxl
# @FileName: 787_4.py



class Solution:

    def dfs(self,u,dst,dis,visited,graph,step,min_val):


        if u == dst:
            tmp = min(min_val[0],dis[u])
            min_val[0] = tmp
        if step == 0 or u not in graph:
            return
        for v in graph[u]:

            if not visited[v]:
                visited[v] = True
                tmp = dis[v]
                dis[v] = min(dis[v],dis[u]+graph[u][v])

                self.dfs(v,dst,dis,visited,graph,step-1,min_val)
                dis[v] = tmp

                visited[v] = False

    def findCheapestPrice(self, n: int, flights , src: int, dst: int, k: int) -> int:

        graph = {}
        for f,t,p in flights:
            if f not in graph:
                graph[f] = {}
            graph[f][t] = p
        dis =[float('inf') for i in range(n)]
        dis[src] = 0
        ans = [float('inf')]
        visited = {i :False for i in range(n)}
        visited[src] = True
        self.dfs(src,dst,dis,visited,graph,k+1,ans)
        if ans[0] == float('inf'):
            return -1
        return int(ans[0])



obj = Solution()
n = 4
flights = [[0,1,1],[0,2,5],[1,2,1],[2,3,1]]
src = 0
dst = 3
k = 1
ans = obj.findCheapestPrice(n,flights,src,dst,k)
print(ans)