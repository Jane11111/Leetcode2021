# -*- coding: utf-8 -*-
# @Time    : 2021-08-03 19:55
# @Author  : zxl
# @FileName: 078_8.py



class Solution:
    def subsets(self, nums ) :

        ans = [[]]

        for num in nums:

            l = len(ans)

            for i in range(l):# 执行一次就是一个时间复杂度，一共有2^n个状态,所以这部分复杂度O(2^n)
                tmp = [item for item in ans[i]]  # 需要重新构造序列，所以每个状态O(N) 复杂度
                tmp.append(num)
                ans.append(tmp)
        return ans