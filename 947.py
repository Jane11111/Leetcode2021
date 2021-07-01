# -*- coding: utf-8 -*-
# @Time    : 2021-07-01 16:05
# @Author  : zxl
# @FileName: 947.py



class Solution:

    def find(self,fa,x):
        if fa[x] == x:
            return x
        fa[x] = self.find(fa,fa[x])
        return fa[x]

    def merge(self,fa,x,y):

        fa[self.find(fa,x)] = self.find(fa,y)



    def removeStones(self, stones ) -> int:

        fa_dic = {}
        graph_dic = {}
        for x,y in stones:
            if y not in graph_dic:
                graph_dic[y] = []
            graph_dic[y].append(x)

            fa_dic[x] = x
        for y in graph_dic:
            p = graph_dic[y][0]
            for x in graph_dic[y]:
                # fa_dic[x] = self.find(fa_dic,p)
                self.merge(fa_dic,x,p)
        sets = set([])
        for x in fa_dic:
            f = self.find(fa_dic,x)
            sets.add(f)

        return len(stones)-len(sets)

obj = Solution()
stones =  [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]

ans = obj.removeStones(stones)
print(ans)

