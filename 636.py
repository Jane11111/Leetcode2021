# -*- coding: utf-8 -*-
# @Time    : 2021-05-15 16:52
# @Author  : zxl
# @FileName: 636.py



class Solution:
    def exclusiveTime(self, n: int, logs ) :


        lst1 = []
        lst2 = []
        ans = [0 for i in range(n)]
        for log in logs:
            arr = log.split(':')
            pid = int(arr[0])
            s = arr[1]
            t = int(arr[2])

            if s == 'start':
                lst1.append([pid,t])
                lst2.append(0)
            else:
                p0,t0 = lst1.pop()
                dt = lst2.pop()
                ans[pid]+= t-t0+1-dt
                if len(lst2)>0: # 把中间这段时间挖去， t0->t的时间段内都已经处理过了
                    lst2[-1]+=(t-t0+1)
        return ans

