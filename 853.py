# -*- coding: utf-8 -*-
# @Time    : 2021-04-15 17:32
# @Author  : zxl
# @FileName: 853.py


class Solution:

    def partition_sort(self,position,speed,i,j):
        if i>=j:
            return

        r = self.partition(position,speed,i,j)
        self.partition_sort(position,speed,i,r-1)
        self.partition_sort(position,speed,r+1,j)

    def partition(self,position,speed,i,j):

        p = i-1
        x = position[j]
        for k in range(i,j):
            if position[k]>=x:
                position[p+1],position[k] = position[k],position[p+1]
                speed[p + 1], speed[k] = speed[k], speed[p + 1]
                p+=1
        position[p + 1], position[j] = position[j], position[p + 1]
        speed[p + 1], speed[j] = speed[j], speed[p + 1]
        return p+1


    def carFleet(self, target , position , speed )  :

        if len(position) == 0:
            return 0


        self.partition_sort(position,speed,0,len(position)-1)

        ans = 1
        reach_time = (target-position[0])/speed[0]
        for i in range(1,len(position)):

            cur_reach_time = (target-position[i])/speed[i]
            if cur_reach_time>reach_time:
                ans+=1
                reach_time = cur_reach_time
        return ans

target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]
obj = Solution()
ans = obj.carFleet(target,position,speed)
print(ans)