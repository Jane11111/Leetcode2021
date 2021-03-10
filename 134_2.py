# -*- coding: utf-8 -*-
# @Time    : 2021-03-09 13:09
# @Author  : zxl
# @FileName: 134_2.py


class Solution(object):


    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        saved_oil = 0
        start = 0
        left_oil = 0
        for i in range(len(gas)):
            if left_oil + gas[i] <cost[i]:

                saved_oil += cost[i]-(left_oil+gas[i])
                start = i+1
                left_oil = 0
            else:
                left_oil += (gas[i]-cost[i])

        if left_oil>=saved_oil and start<len(gas):
            return start
        else:
            return -1

obj = Solution()
gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
f = obj.canCompleteCircuit(gas,cost)
print(f)

