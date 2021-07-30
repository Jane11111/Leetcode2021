# -*- coding: utf-8 -*-
# @Time    : 2021-07-28 21:04
# @Author  : zxl
# @FileName: 797_2.py



class Solution:

    def dfs(self,graph,visited,n,cur,dic):

        if cur == n-1:
            dic[cur] = [[cur]]

        if cur in dic:
            return dic[cur]

        lst = []
        for neighbor in graph[cur]:
            if not visited[neighbor]:

                visited[neighbor] = True
                sub_paths = self.dfs(graph,visited,n,neighbor,dic)
                for path in sub_paths: #  当前到n-1的所有路径
                    tmp = [item for item in path]
                    tmp.insert(0,cur)
                    lst.append(tmp)

                visited[neighbor] = False
        dic[cur] = lst
        return lst


    def allPathsSourceTarget(self, graph ) :


        n = len(graph)
        visited = {i:False for i in range(n)}
        visited[0] = True
        dic = {}
        ans = self.dfs(graph,visited,n,0,dic)
        return ans

obj = Solution()
graph =   [[1,3],[2],[3],[]]
ans = obj.allPathsSourceTarget(graph)
print(ans)


