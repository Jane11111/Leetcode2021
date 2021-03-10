# -*- coding: utf-8 -*-
# @Time    : 2021-03-08 17:49
# @Author  : zxl
# @FileName: 1306.py


class Solution(object):

    def recursiveSearch(self,arr,start,dic):

        if start < 0 or start >= len(arr):
            return False
        if arr[start] == 0:
            return True

        idx1 = start - arr[start]
        idx2 = start + arr[start]

        res = False
        if idx1 in dic and idx2 in dic:
            return res

        if idx1 not in dic:
            dic[idx1] = True
            f = self.recursiveSearch(arr,idx1,dic)
            if f :
                return f


        if idx2 not in dic:
            dic[idx2] = True
            f = self.recursiveSearch(arr,idx2,dic)
            if f :
                return f


        return res



    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """

        res = self.recursiveSearch(arr,start,{})
        return res


arr = [3,0,2,1,2]
start = 2

obj = Solution()
res = obj.canReach(arr,start)
print(res)

