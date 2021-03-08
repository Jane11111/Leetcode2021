# -*- coding: utf-8 -*-
# @Time    : 2021-03-08 16:16
# @Author  : zxl
# @FileName: I1611.py


class Solution(object):



    def divingBoard(self, shorter, longer, k):
        """
        :type shorter: int
        :type longer: int
        :type k: int
        :rtype: List[int]
        """

        if k == 0:
            return []
        if shorter== longer:
            return [k*shorter]
        res = []
        for i in range(k+1):
            res.append(i*longer+(k-i)*shorter)
        return res



obj = Solution()
res = obj.divingBoard(1,2,3)
print(res)