# -*- coding: utf-8 -*-
# @Time    : 2021-06-07 21:22
# @Author  : zxl
# @FileName: 886_2.py


class Solution:
    def possibleBipartition(self, n: int, dislikes ) -> bool:


        groups = [-1 for i in range(n+1)]

        dic = {i:[] for i in range(1,n+1)}
        for x, y in dislikes:
            dic[x].append(y)
            dic[y].append(x)

        for i in range(1,n+1):
            if groups[i] != -1:
                continue
            groups[i] = 0
            st = [i]
            v_st = [0]
            while len(st)!=0:
                node = st.pop(0)
                v = v_st.pop(0)

                for dis_node in dic[node]:

                    if groups[dis_node] == -1:
                        st.append(dis_node)
                        groups[dis_node] = 1-v
                        v_st.append(1-v)
                    else:
                        if groups[dis_node] != 1-v:
                            return False
        return True




N = 5
dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
obj = Solution()
ans = obj.possibleBipartition(N,dislikes)
print(ans)
