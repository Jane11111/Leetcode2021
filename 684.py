# -*- coding: utf-8 -*-
# @Time    : 2021-03-26 17:53
# @Author  : zxl
# @FileName: 684.py


class Solution:
    def findRedundantConnection(self, edges ) :

        n = len(edges)


        neighbor_dic = {i:{} for i in range(1,n+1)}
        freq = [0 for i in range(0,n+1)]
        for x,y in edges:
            neighbor_dic[x][y] = True
            neighbor_dic[y][x] = True
            freq[x] +=1
            freq[y]+=1


        lst = []
        for i in range(1,n+1):
            if freq[i] == 1:
                lst.append(i)
                freq[i] = 0

        while len(lst)>0:

            l = len(lst)
            while l:
                u = lst.pop(0)
                l-=1
                for v in neighbor_dic[u]:
                    if freq[v]>0:
                        freq[v]-=1
                        if freq[v]==1:
                            lst.append(v)
                            freq[v] = 0



        for i in range(n-1,-1,-1):
            x,y = edges[i]
            if freq[x]!=0 and freq[y]!=0:
                return [x,y]



