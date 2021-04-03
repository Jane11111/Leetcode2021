# -*- coding: utf-8 -*-
# @Time    : 2021-04-02 13:00
# @Author  : zxl
# @FileName: 870.py

class Solution(object):
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        n = len(A)
        sorted_idx = sorted(range(n),key = lambda k:B[k])
        A.sort()

        ans = [-1 for i in range(n)]
        used = [False for i in range(n)]

        i = 0

        for idx in sorted_idx:

            while i<n and A[i]<=B[idx]:
                i+=1
            if i>=n:
                break
            used[i] = True
            ans[idx] = A[i]
            i+=1

        i = 0
        for k in range(n):
            if ans[k] == -1:
                while used[i]:
                    i+=1
                ans[k] = A[i]
                used[i] = True
        return ans
obj = Solution()
A = [2,0,4,1,2]
B = [1,3,0,0,2]
ans = obj.advantageCount(A,B)
print(ans)