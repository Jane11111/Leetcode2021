# -*- coding: utf-8 -*-
# @Time    : 2021-03-09 11:57
# @Author  : zxl
# @FileName: 134.py


class Solution(object):

    def judge(self,gas,cost,start_idx,start_gas):

        for i in range(0,len(gas)):
            idx = (start_idx+i)%len(gas)
            if start_gas + gas[idx] < cost[idx]:
                return False
            else:
                start_gas = start_gas+gas[idx]-cost[idx]
        return True

    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        for i in range(len(gas)):
            if self.judge(gas,cost,i,0):
                return i
        return -1

obj = Solution()
gas = [2,3,4]
cost = [3,4,3]
f = obj.canCompleteCircuit(gas,cost)
print(f)

