# -*- coding: utf-8 -*-
# @Time    : 2021-07-01 15:36
# @Author  : zxl
# @FileName: 851.py



class Solution:

    def dfs(self,graph_dic,res_dic,i,quiet):
        if i in res_dic:
            return res_dic[i]
        if i not in graph_dic:
            res_dic[i] = i
            return i
        min_quiet = quiet[i]
        person = i
        for v in graph_dic[i]:

            cur_person = self.dfs(graph_dic,res_dic,v,quiet)
            if quiet[cur_person]<min_quiet:
                min_quiet = quiet[cur_person]
                person = cur_person
        res_dic[i] = person
        if type(person) == dict:
            print('i am here')
        return person



    def loudAndRich(self, richer , quiet ) :

        n = len(quiet)
        ans = [i for i in range(n)]
        res_dic = {}

        graph_dic = {}
        for x,y in richer:

            if y not in graph_dic:
                graph_dic[y] = []
            graph_dic[y].append(x)

        for i in range(n):
            v = self.dfs(graph_dic,res_dic,i,quiet)
            ans[i] = v
        return ans


obj = Solution()
richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]]
quiet = [3,2,5,4,6,1,7,0]
ans = obj.loudAndRich(richer,quiet)
print(ans)




