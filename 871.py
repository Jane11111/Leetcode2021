# -*- coding: utf-8 -*-
# @Time    : 2021-05-27 09:41
# @Author  : zxl
# @FileName: 871.py


class Solution:


    def recGo(self,idx,target,fuel,stations):

        cur_pos = stations[idx][0]
        can_add = stations[idx][1]

        if cur_pos+fuel>=target:
            return 0
        elif cur_pos+fuel+can_add>=target:
            return 1
        elif idx+1>=len(stations) or cur_pos+fuel+can_add< stations[idx+1][0]:
            return -1

        ans = float('inf')
        for i in range(idx+1,len(stations)):

            if cur_pos+fuel+can_add<stations[i][0]:
                break

            n1 = self.recGo(i,target,fuel+can_add-(stations[i][0]-cur_pos),stations)
            if n1>=0:
                ans = min(ans,n1+1)
        if ans == float('inf') :
            ans = -1
        return ans

    def minRefuelStops(self, target: int, startFuel: int, stations ) -> int:

        stations.insert(0,[0,startFuel])

        ans = self.recGo(0,target,0,stations)

        if ans>0:
            ans -=1
        return ans

obj = Solution()
target = 100
startFuel = 1
stations = [ ]
ans = obj.minRefuelStops(target,startFuel,stations)
print(ans)