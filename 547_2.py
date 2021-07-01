# -*- coding: utf-8 -*-
# @Time    : 2021-07-01 11:31
# @Author  : zxl
# @FileName: 547_2.py


class Solution:

    def findCircleNum(self, isConnected) -> int:

        n = len(isConnected)

        visited = {i:False for i in range(n)}
        count = 0

        for i in range(n):
            if visited[i]:
                continue
            count += 1

            lst = [i]
            visited[i] = True
            while len(lst)>0:
                cur = lst.pop()
                for j in range(n):
                    if isConnected[cur][j] and not visited[j]:
                        visited[j] = True
                        lst.append(j)
        return count



