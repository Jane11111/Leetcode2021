# -*- coding: utf-8 -*-
# @Time    : 2021-03-31 10:54
# @Author  : zxl
# @FileName: 802.py


class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """

        lst = []
        visited = {}
        while True:
            start_idx = len(lst)
            for i in range(len(graph)-1,-1,-1):
                if i in visited:
                    continue
                if len(graph[i]) == 0:
                    lst.append(i)
                    visited[i] = True
                else:
                    f = True
                    for j in range(len(graph[i])):
                        if graph[i][j] not in visited:
                            f=False
                            continue
                    if f:
                        lst.append(i)
                        visited[i] = True


            if start_idx == len(lst):
                break

            # for i in range(start_idx,len(lst)):
            #     num = lst[i]
            #     for j in range(len(graph)):
            #         if j in visited:
            #             continue
            #         if num in graph[j]:
            #             graph[j].remove(num)
            #             continue
        lst.sort()
        return lst

obj = Solution()
graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
ans = obj.eventualSafeNodes(graph)
print(ans)



