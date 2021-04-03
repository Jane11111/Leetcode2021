# -*- coding: utf-8 -*-
# @Time    : 2021-03-25 19:53
# @Author  : zxl
# @FileName: 077.py


class Solution(object):

    def recursiveCombine(self,lst,k):
        ans = []

        if k>len(lst):
            return ans

        if k == 1:
            for item in lst:
                ans.append([item])
            return ans
        for i in range(len(lst)):
            num = lst[i]
            sub_ans_lst = self.recursiveCombine(lst[i+1:],k-1)
            for sub_ans in sub_ans_lst:
                sub_ans.insert(0,num)
                ans.append(sub_ans)
        return ans

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        lst = [i for i in range(1,n+1)]
        ans = self.recursiveCombine(lst,k)
        return ans

obj = Solution()
n = 4
k = 2
ans = obj.combine(n,k)
print(ans)


