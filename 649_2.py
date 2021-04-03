# -*- coding: utf-8 -*-
# @Time    : 2021-04-02 17:23
# @Author  : zxl
# @FileName: 649_2.py


class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """

        R_indices = []
        D_indices = []
        for i in range(len(senate)):
            if senate[i] == 'R':
                R_indices.append(i)
            else:
                D_indices.append(i)
        n = len(senate)
        while len(R_indices) > 0 and len(D_indices) > 0:

            if R_indices[0] < D_indices[0]:
                D_indices.pop(0)
                idx = R_indices.pop(0)
                R_indices.append(idx+n)
            else:
                R_indices.pop(0)
                idx = D_indices.pop(0)
                D_indices.append(idx+n)
        if len(R_indices) == 0:
            return 'Dire'
        else:
            return 'Radiant'

obj = Solution()
senate = "RDD"
ans = obj.predictPartyVictory(senate)
print(ans)