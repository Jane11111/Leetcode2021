# -*- coding: utf-8 -*-
# @Time    : 2021-03-31 10:34
# @Author  : zxl
# @FileName: 785.py


class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """

        n = len(graph)
        nums = [-1 for i in range(n)]

        for i in range(n):
            if nums[i] != -1:
                continue
            nums[i] = 0
            Q = [i]
            while len(Q) > 0:
                u = Q.pop(0)
                last_num = nums[u]
                for v in graph[u]:
                    if nums[v] == -1:
                        Q.append(v)
                        nums[v] = 1-last_num
                    elif nums[v] != 1-last_num:
                        return False
        return True

obj = Solution()
graph = [[1,3],[0,2],[1,3],[0,2]]
ans = obj.isBipartite(graph)
print(ans)





