# -*- coding: utf-8 -*-
# @Time    : 2021-07-27 21:19
# @Author  : zxl
# @FileName: 134_4.py



class Solution:
    def canCompleteCircuit(self, gas, cost ) -> int:

        n = len(gas)
        needtosave = 0
        left = 0

        start = 0

        for i in range(n):
            if left+gas[i]>=cost[i]:
                left = left+gas[i]-cost[i]
            else:
                start = i+1
                needtosave += cost[i] - (left+gas[i])
                left = 0


        if left>=needtosave :
            return start
        return -1



