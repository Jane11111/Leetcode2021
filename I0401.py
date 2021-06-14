# -*- coding: utf-8 -*-
# @Time    : 2021-06-07 21:56
# @Author  : zxl
# @FileName: I0401.py

class Solution:


    def dfs(self,s_id,e_id,visited,dic):

        if s_id == e_id:
            return True
        visited[s_id] = True
        for n_id in dic[s_id]:
            if not visited[n_id] :
                f = self.dfs(n_id,e_id,visited,dic)
                if f:
                    return f
        # visited[s_id] = False
        return False

    def findWhetherExistsPath(self, n: int, graph , start: int, target: int) -> bool:

        visited = {i:False for i in range(n)}
        dic = {i:{} for i in range(n)}

        for x,y in graph:
            if y!=x:
                dic[x][y] = True

        f = self.dfs(start,target,visited,dic)
        return f


n = 5
graph = [[0, 1], [0, 2], [0, 4], [0, 4], [0, 1], [1, 3], [1, 4], [1, 3], [2, 3], [3, 4]]

start = 0
target = 4
obj = Solution()
ans = obj.findWhetherExistsPath(n,graph,start,target)
print(ans)





