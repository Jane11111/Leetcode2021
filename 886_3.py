# -*- coding: utf-8 -*-
# @Time    : 2021-06-07 21:34
# @Author  : zxl
# @FileName: 886_3.py





class Solution:


    def dfs(self,n_id,visited,dic):

        v = visited[n_id]

        for dis_id in dic[n_id]:
            if visited[dis_id] == v:
                return False
            elif visited[dis_id] == -1:
                visited[dis_id] = 1-v
                self.dfs(dis_id,visited,dic)
        return True

    def possibleBipartition(self, n: int, dislikes ) -> bool:

        visited = [-1 for i in range(n+1)]

        dic = {i:[] for i in range(1,n+1)}

        for x,y in dislikes:
            dic[x].append(y)
            dic[y].append(x)
        for i in range(1,n+1):
            if visited[i]==-1:
                visited[i] = 0
                f = self.dfs(i,visited,dic)
                if not f:
                    return f
        return True




N = 5
dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
obj = Solution()
ans = obj.possibleBipartition(N,dislikes)
print(ans)



