# -*- coding: utf-8 -*-
# @Time    : 2021-07-01 13:58
# @Author  : zxl
# @FileName: 787_2.py

# 超时

class Solution:
    def findCheapestPrice(self, n: int, flights , src: int, dst: int, k: int) -> int:

        dic = {}
        ans = float('inf')

        for u, v, p in flights:
            if u not in dic:
                dic[u] = {}
            dic[u][v] = p

        lst = [[src,0,0]]

        while len(lst)>0:

            idx = -1
            min_val = float('inf')
            for i in range(len(lst)): # 应该是这里的原因，超时
                if  lst[i][2]<min_val:
                    min_val = lst[i][2]
                    idx = i
            u,step,d = lst.pop(idx)
            if u == dst:
                return ans

            if u not in dic or step == k+1:
                continue
            for v in dic[u]:
                p = dic[u][v]
                lst.append([v,step+1,d+p])
        if ans == float('inf'):
            return -1
        return ans


obj = Solution()
n = 3
edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
k = 1
ans = obj.findCheapestPrice(n,edges,src,dst,k)
print(ans)

