# -*- coding: utf-8 -*-
# @Time    : 2021-06-07 22:20
# @Author  : zxl
# @FileName: I0401_2.py



class Solution:




    def findWhetherExistsPath(self, n: int, graph , start: int, target: int) -> bool:

        visited = {i:False for i in range(n)}
        dic = {i:{} for i in range(n)}

        for x,y in graph:
            if y!=x:
                dic[x][y] = True

        st = [start]
        while len(st)>0:

            cur_id = st.pop(0)
            if cur_id == target:
                return True
            for n_id in dic[cur_id]:
                if not visited[n_id]:
                    visited[n_id] = True
                    st.append(n_id)

        return False



n = 5
graph =  [[0, 1], [0, 2], [1, 2], [1, 2]]
start = 0
target = 2
obj = Solution()
ans = obj.findWhetherExistsPath(n,graph,start,target)
print(ans)
