# -*- coding: utf-8 -*-
# @Time    : 2021-07-19 11:15
# @Author  : zxl
# @FileName: 436_2.py


import numpy as np
class Solution:

    def bisearch(self,lst,sortedidx,target):

        if target > lst[sortedidx[-1]]:
            return -1

        l = 0
        h = len(sortedidx)

        while l<h:

            m = (l+h)//2

            if lst[sortedidx[m]]<target:
                l = m+1
            else:
                h = m

        return int(sortedidx[l])


    def findRightInterval(self, interval ) :

        lst = []
        for s,e in interval:
            lst.append(s)

        sortedidx = np.argsort(lst)

        ans = []
        for s,e in interval:
            idx = self.bisearch(lst,sortedidx,e)
            ans.append(idx)
        return ans






