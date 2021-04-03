# -*- coding: utf-8 -*-
# @Time    : 2021-03-26 13:10
# @Author  : zxl
# @FileName: 797.py

class Solution(object):

    def recursiveVisit(self,graph,visited,cur,target):

        if cur == target:
            return [[target]]

        path_lst = []
        neighbors = graph[cur]
        for neighbor in neighbors:
            if not visited[neighbor]:
                visited[neighbor] = True
                sub_path_lst = self.recursiveVisit(graph,visited,neighbor,target)
                visited[neighbor] = False
                for path in sub_path_lst:
                    # path.insert(0,neighbor)
                    path.insert(0,cur)
                    path_lst.append(path)

        return path_lst




    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """


        n = len(graph)
        visited = {i: False for i in range(n)}

        ans = self.recursiveVisit(graph,visited,0,n-1)
        return ans

obj = Solution()
graph = [[1,3],[2],[3],[]]
ans = obj.allPathsSourceTarget(graph)
print(ans)
