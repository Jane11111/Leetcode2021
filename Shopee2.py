# -*- coding: utf-8 -*-
# @Time    : 2021-07-05 15:29
# @Author  : zxl
# @FileName: Shopee2.py


# 通过50%， 可能因为超时
#dfs 回溯

class Solution:

    def isValid(self,x,y,m,n):


        return x>=0 and x<m and y>=0 and y<n

    def dfs(self,rooms, used, x,y, m,n,endPoint,memo):



        if x == endPoint[0] and y == endPoint[1]:
            if rooms[x][y] <=0:
                return abs(rooms[x][y])+1
            else:
                return 1
        ans = float('inf')


        for next_x,next_y in [(x-1,y),(x,y-1),(x+1,y),(x,y+1)]:
            if not self.isValid(next_x,next_y,m,n):
                continue
            if not used[next_x][next_y]:

                used[next_x][next_y] = True

                points = self.dfs(rooms,used,next_x,next_y,m,n,endPoint,memo)
                # if x==0 and y == 0:
                #     print('i am here')
                if points!=float('inf'): # 有路径

                    if rooms[x][y]<=0:
                        ans = min(ans, abs(rooms[x][y])+points)
                    else:
                        if rooms[x][y] >= points:
                            ans = min(ans,1)
                        else:
                            ans = min(ans, abs(rooms[x][y]-points))


                used[next_x][next_y] = False
                # if ans == 1:
                #     break

        return ans





    def minimumInitHealth(self, rooms, startPoint, endPoint) :

        m = len(rooms)
        n = len(rooms[0])
        used = []
        for i in range(m):
            used.append([False for j in range(n)])
        ans = self.dfs(rooms,used,startPoint[0],startPoint[1],m,n,endPoint,{})
        return ans


obj = Solution()
rooms = [[100]]
startPoint = [0,0]
endPoint = [0,0]
ans = obj.minimumInitHealth(rooms,startPoint,endPoint)
print(ans)