# -*- coding: utf-8 -*-
# @Time    : 2021-06-22 10:07
# @Author  : zxl
# @FileName: 365_2.py




class Solution:

    def gcd(self,x,y):

        x,y = (y,x) if y>x else (x,y)

        z = x%y
        while z!=0:
            x = y
            y = z
            z = x%y


        return y


    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:

        if jug1Capacity+jug2Capacity<targetCapacity:
            return False

        if jug1Capacity == 0 or jug2Capacity == 0:
            return targetCapacity==0 or jug1Capacity+jug2Capacity == targetCapacity

        g = self.gcd(jug1Capacity,jug2Capacity)
        return targetCapacity%g == 0