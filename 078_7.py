# -*- coding: utf-8 -*-
# @Time    : 2021-07-17 21:11
# @Author  : zxl
# @FileName: 078_7.py


class Solution:
    def subsets(self, nums ) :

        ans = [[]]

        for num in nums:
            l = len(ans)
            for i in range(l):
                tmp = [item for item in ans[i]]
                tmp.append(num)
                ans.append(tmp)
        return ans