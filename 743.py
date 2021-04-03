# -*- coding: utf-8 -*-
# @Time    : 2021-03-30 21:01
# @Author  : zxl
# @FileName: 743.py


class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """

        visited = [False for i in range(n+1)]
        shortest = [float('inf') for i in range(n+1)]

        dic = {}
        for u,v,w in times:
            if u not in dic:
                dic[u] = {}
            dic[u][v] = w


        # visited[k] = True
        shortest[k] = 0
        while True:
            u = 0
            for i in range(1,n+1,1):
                if not visited[i] and shortest[i]<shortest[u]:
                    u = i
            if u == 0:
                break
            visited[u] = True
            if u not in dic:
                continue
            for v in dic[u]:
                w = dic[u][v]
                shortest[v] = min(shortest[v],shortest[u]+w)

        max_time = 0
        for i in range(1,n+1,1):
            if shortest[i] == float('inf'):
                return -1
            max_time = max(max_time,shortest[i])
        return max_time

obj = Solution()
times = [[1,2,1]]
n = 2
k = 2
ans = obj.networkDelayTime(times,n,k)
print(ans)









