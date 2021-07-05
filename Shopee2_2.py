# -*- coding: utf-8 -*-
# @Time    : 2021-07-05 15:59
# @Author  : zxl
# @FileName: Shopee2_2.py



import heapq
class Solution:

    def isValid(self,x,y,m,n):


        return x>=0 and x<m and y>=0 and y<n


    def minimumInitHealth(self, rooms, startPoint, endPoint):


        m = len(rooms)
        n = len(rooms[0])

        dis = []
        for i in range(m):
            dis.append([float('inf') for j in range(n)])

        x,y = endPoint
        if rooms[x][y]<=0:
            h = abs(rooms[x][y])+1

        else:
            h = 1
        lst = []
        heapq.heappush(lst,[h,x,y])

        while len(lst)>0:

            p,x,y = heapq.heappop(lst)
            if x == startPoint[0] and y == startPoint[1]:
                return p

            for next_x,next_y in [[x-1,y],[x,y-1],[x+1,y],[x,y+1]]:
                if not self.isValid(next_x,next_y,m,n):
                    continue
                if rooms[next_x][next_y] <= 0:
                    new_p = abs(rooms[next_x][next_y]) + p
                else:
                    if rooms[next_x][next_y] >= p:
                        new_p = 1
                    else:
                        new_p = abs(rooms[next_x][next_y] - p)

                if dis[next_x][next_y] == float('inf'):
                    dis[next_x][next_y] = new_p
                    heapq.heappush(lst,[new_p,next_x,next_y])
                else:
                    dis[next_x][next_y] = min(new_p,dis[next_x][next_y])


obj = Solution()
rooms = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
startPoint = [0,0]
endPoint = [2,2]
ans = obj.minimumInitHealth(rooms,startPoint,endPoint)
print(ans)




