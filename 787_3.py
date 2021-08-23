# -*- coding: utf-8 -*-
# @Time    : 2021-08-15 10:49
# @Author  : zxl
# @FileName: 787_3.py


class Solution:
    def findCheapestPrice(self, n: int, flights , src: int, dst: int, k: int) -> int:

        dis = [float('inf') for i in range(n)]
        dis[src] = 0

        while k+1:
            old_dis = [item for item in dis]
            for f,t,p in flights:
                if dis[f]!=float('inf'):
                    dis[t] = min(old_dis[f]+p,dis[t])

            k -=1
        if dis[dst] == float('inf'):
            return -1
        return int(dis[dst])

obj = Solution()
n = 4
flights = [[0,1,1],[0,2,5],[1,2,1],[2,3,1]]
src = 0
dst = 3
k = 1
ans = obj.findCheapestPrice(n,flights,src,dst,k)
print(ans)

