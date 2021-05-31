# -*- coding: utf-8 -*-
# @Time    : 2021-05-27 10:01
# @Author  : zxl
# @FileName: 871_2.py



class Solution:

    def minRefuelStops(self, target: int, startFuel: int, stations) -> int:

        stations.insert(0,[0,startFuel])
        # dp[i][j] 经过j个station到达第i个station剩余的最大油量

        if target<=startFuel:
            return 0

        dp = []

        ans = float('inf')
        for i in range(len(stations)):
            dp.append([-1 for j in range(len(stations)+1)])
        dp[0][0] = 0
        for i in range(1,len(stations)):
            if stations[i][0]>startFuel:
                break
            dp[i][0] = startFuel-stations[i][0]
            if dp[i][0]!=-1 :
                # if dp[i][0]>=target:
                #     ans = min(ans,0)
                if dp[i][0]+stations[i][1]>=target-stations[i][0]:
                    ans = min(ans,1)




        for i in range(1,len(stations)):
            for j in range(1,len(stations)):
                max_fuel = -1
                for k in range(i):

                    if dp[k][j-1] != -1 and dp[k][j-1]+stations[k][1]>=stations[i][0]-stations[k][0]:
                        max_fuel = max(max_fuel,dp[k][j-1]+stations[k][1]-(stations[i][0]-stations[k][0]) )

                dp[i][j] = max_fuel
                if max_fuel != -1:

                    # if max_fuel >= target-stations[i][0]:
                    #     ans = min(ans,j)
                    if max_fuel + stations[i][1] >= target-stations[i][0]:
                        ans = min(ans,j+1)

        if ans == float('inf'):
            ans = -1
        return ans






obj = Solution()
target = 100
startFuel = 25
stations = [[25,25],[50,25],[75,25]]
ans = obj.minRefuelStops(target,startFuel,stations)
print(ans)