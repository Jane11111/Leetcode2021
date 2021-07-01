# -*- coding: utf-8 -*-
# @Time    : 2021-07-01 15:11
# @Author  : zxl
# @FileName: 782_3.py


# TODO 超时

class Solution:


    def dfs(self,cur_src,dst, dic,k,cur_dist,cur_k,visited ):

        ans = float('inf')

        if cur_src == dst:
            return cur_dist
        if cur_k == k+1 or cur_src not in dic:
            return ans

        for v in dic[cur_src]:

            if not visited[v]:
                p = dic[cur_src][v]
                if cur_dist+p>ans:
                    continue

                visited[v] = True

                dist = self.dfs(v,dst, dic,k,cur_dist+p,cur_k+1,visited)
                ans = min(ans,dist)
                visited[v] = False
        return ans





    def findCheapestPrice(self, n: int, flights , src: int, dst: int, k: int) -> int:

        dic = {}
        for u, v, p in flights:
            if u not in dic:
                dic[u] = {}
            dic[u][v] = p
        visited = {i:False for i in range(n)}

        ans = self.dfs(src,dst, dic,k,0,0,visited)
        if ans == float('inf'):
            return -1
        return ans



