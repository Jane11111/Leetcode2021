# -*- coding: utf-8 -*-
# @Time    : 2021-06-10 17:07
# @Author  : zxl
# @FileName: 1129.py




class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges , blue_edges ) :



        arr = [-1 for i in range(n)]

        arr[0] = 0

        st = [[0,-1]]
        dis_lst = [0]

        red_edge_dic = {i:{} for i in range(n)}
        for x,y in red_edges:
            if y not in red_edge_dic[x]:
                red_edge_dic[x][y] = 0
            red_edge_dic[x][y] +=1
        blue_edge_dic = {i:{} for i in range(n)}
        for x,y in blue_edges:
            if y not in blue_edge_dic[x]:
                blue_edge_dic[x][y] = 0
            blue_edge_dic[x][y] +=1
        red_visited = [False for i in range(n)]
        blue_visited = [False for i in range(n)]
        while len(st)>0:

            u, c = st.pop(0)
            d = dis_lst.pop(0)

            if c == 0 or c == -1:
                for v in blue_edge_dic[u]:
                    if v == 0:
                        continue
                    if not blue_visited[v]:
                        st.append([v,1])
                        if arr[v] == -1:
                            arr[v] = d+1
                        blue_visited[v] = True
                        dis_lst.append(d+1)
            if c == 1 or c == -1:
                for v in red_edge_dic[u]:
                    if v == 0:
                        continue
                    if not red_visited[v]:
                        st.append([v,0])
                        if arr[v] == -1:
                            arr[v] = d+1
                        red_visited[v] =True
                        dis_lst.append(d+1)
        return arr




