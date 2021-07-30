# -*- coding: utf-8 -*-
# @Time    : 2021-07-27 19:44
# @Author  : zxl
# @FileName: 134_3.py




class Solution:
    def canCompleteCircuit(self, gas, cost ) -> int:

        n = len(gas)
        start = 0

        while start < n:

            i = start
            count = 0

            left = 0
            while left + gas[i%n]>=cost[i%n] and i<start+n:
                left = left+gas[i%n]-cost[i%n]
                i += 1
                count+=1

            if count == n:
                return start
            # start = max(i+1,start+1)
            i%=n
            if i<start:
                break
            start = i+1

        return -1

obj = Solution()
gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]
ans = obj.canCompleteCircuit(gas,cost)
print(ans)








