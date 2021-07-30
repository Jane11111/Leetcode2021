# -*- coding: utf-8 -*-
# @Time    : 2021-07-19 09:58
# @Author  : zxl
# @FileName: 636_2.py


class Solution:
    def exclusiveTime(self, n: int, logs ) :

        arr = [0 for i in range(n)]

        st = []

        for i in range(0,len(logs)):

            cur_log = logs[i]

            curid,curtag,curtime = cur_log.split(':')

            curid = int(curid)
            curtime = int(curtime)

            if curtag == 'start':
                st.append([curid,curtime])
            else:
                lastid,lasttime = st.pop()

                interval_time = curtime-lasttime+1
                arr[curid] += interval_time

                if len(st)>0:
                    arr[st[-1][0]]-=interval_time
        return arr




