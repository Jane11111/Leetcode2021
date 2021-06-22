# -*- coding: utf-8 -*-
# @Time    : 2021-06-21 20:29
# @Author  : zxl
# @FileName: 365.py



class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:

        dic = {}

        st = [(0,0)]


        while len(st)>0:

            x,y = st.pop()
            if x in dic and y in dic[x]:
                continue
            if x not in dic:
                dic[x] = {}
            dic[x][y] = True

            if x==targetCapacity or y == targetCapacity or x+y == targetCapacity:
                return True

            st.append([x,jug2Capacity])
            st.append([jug1Capacity,y])
            st.append([0,y])
            st.append([x,0])
            st.append([x-min(x,jug2Capacity-y),y+min(jug2Capacity-y,x)])
            st.append([x+min(jug1Capacity-x,y),y-min(y,jug1Capacity-x)])
        return False