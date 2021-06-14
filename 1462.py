# -*- coding: utf-8 -*-
# @Time    : 2021-06-10 21:21
# @Author  : zxl
# @FileName: 1462.py



class Solution:


    def dfs(self,s,path_dic,dic):

        if s in path_dic:
            return path_dic[s]

        ans = []
        for n in dic[s]:
            lst = self.dfs(n,path_dic,dic)
            lst.insert(0,n)
            ans.extend(lst)
        path_dic[s] = list(set(ans))
        return path_dic[s]




    def checkIfPrerequisite(self, numCourses: int, prerequisites , queries ) :


        dic = {i:[] for i in range(numCourses)}
        for x,y in prerequisites:
            dic[x].append(y)

        path_dic = {}
        for i in range(numCourses):
            self.dfs(i,path_dic,dic)

        new_dic = {}
        for k in path_dic:
            new_dic[k] = {}
            for v in path_dic[k]:
                new_dic[k][v] = True
        ans = []
        for i,j in queries:
            if j in new_dic[i]:
                ans.append(True)
            else:
                ans.append(False)
        return ans


obj = Solution()
numCourse = 5
prerequisites= [[0,1],[1,2],[2,3],[3,4]]
queries = [[0,4],[4,0],[1,3],[3,0]]
ans = obj.checkIfPrerequisite(numCourse,prerequisites,queries)
print(ans)