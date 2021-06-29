# -*- coding: utf-8 -*-
# @Time    : 2021-06-29 11:48
# @Author  : zxl
# @FileName: 149_2.py


class Solution:

    def gcd(self,a,b):

        if a<b:
            return self.gcd(b,a)
        while b!=0:
            tmp = a%b
            a=b
            b = tmp
        return a


    def calK(self,x1,y1,x2,y2):
        if x1 == x2:
            return x1,float('inf')
        if y1 == y2:
            return float('inf'),y1

        delta_x = (x2-x1)
        delta_y = (y2-y1)
        neg = delta_x*delta_y<0

        delta_x = abs(delta_x)
        delta_y = abs(delta_y)

        gcd = self.gcd(delta_x,delta_y)

        delta_x/=gcd
        delta_y/=gcd

        if neg:
            delta_x = -delta_x
        return delta_x,delta_y


    def maxPoints(self, points) -> int:
        if len(points) == 1:
            return 1


        ans = 0
        for i in range(len(points)):
            x1,y1 = points[i]
            dic = {}
            for j in range(i+1,len(points)):
                x2,y2 = points[j]

                delta_x,delta_y = self.calK(x1,y1,x2,y2)

                if delta_x not in dic:
                    dic[delta_x] = {}
                if delta_y not in dic[delta_x]:
                    dic[delta_x][delta_y] = 0
                dic[delta_x][delta_y]+=1
                ans = max(ans,dic[delta_x][delta_y])
        # ans = 0
        # for k1 in dic:
        #     for k2 in dic[k1]:
        #         ans = max(ans,dic[k1][k2])
        return ans+1

obj = Solution()
points =  [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
ans = obj.maxPoints(points)
print(ans)
