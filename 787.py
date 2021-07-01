# -*- coding: utf-8 -*-
# @Time    : 2021-07-01 12:05
# @Author  : zxl
# @FileName: 787.py




class Solution:
    def findCheapestPrice(self, n: int, flights , src: int, dst: int, k: int) -> int:

        arr = [float('inf') for i in range(n)]
        dic = {}

        for u,v,p in flights:
            if u not in dic:
                dic[u] = {}
            dic[u][v] = p

        arr[src] = 0
        lst = [src]
        while k+1:
            k-=1
            arr_new = [item for item in arr]

            l = len(lst)
            for i in range(l):
                u = lst[i]
                if u not in dic:
                    continue
                for v in dic[u]:
                    p = dic[u][v]
                    if arr[v] == float('inf'):
                        lst.append(v)
                    arr_new[v] = min(arr[u]+p,arr_new[v])
            arr = arr_new
        if arr[dst] == float('inf'):
            return -1
        return arr[dst]











