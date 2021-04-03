# -*- coding: utf-8 -*-
# @Time    : 2021-03-31 13:18
# @Author  : zxl
# @FileName: 841.py


class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """

        n = len(rooms)
        visited = [False for i in range(n)]
        Q = [0]
        visited[0] = True
        while len(Q) > 0:
            u = Q.pop(0)
            for v in rooms[u]:
                if not visited[v]:
                    Q.append(v)
                    visited[v] = True
        for i in range(n):
            if not visited[i]:
                return False
        return True
rooms = [[1,3],[3,0,1],[2],[0]]
obj = Solution()
ans = obj.canVisitAllRooms(rooms)
print(ans)
