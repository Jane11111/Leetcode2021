# -*- coding: utf-8 -*-
# @Time    : 2021-05-27 11:24
# @Author  : zxl
# @FileName: 871_3.py



class Solution:

    def minRefuelStops(self, target: int, startFuel: int, stations) -> int:

        stations.insert(0,[0,startFuel])

        dp = [0 for i in range(len(stations))]
        dp[0] = startFuel

        for i in range(1,len(stations)): # 看到一个新的加油站
            for j in range(i,-1,-1): # 要倒着来
                if dp[j] >=stations[i][0]:
                    dp[j+1] = max(dp[j+1],dp[j]+stations[i][1])

        for i in range(len(stations)):
            if dp[i]>=target:
                return i
        return -1



obj = Solution()
target = 1000
startFuel = 83
stations = [[25,27],[36,187],[140,186],[378,6],[492,202],[517,89],[579,234],[673,86],[808,53],[954,49]]
ans = obj.minRefuelStops(target,startFuel,stations)
print(ans)