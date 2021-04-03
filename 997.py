# -*- coding: utf-8 -*-
# @Time    : 2021-04-01 20:41
# @Author  : zxl
# @FileName: 997.py


class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """

        out_degree = [0 for i in range(N+1)]
        in_degree = [0 for i in range(N + 1)]

        for x,y in trust:
            out_degree[x] += 1
            in_degree[y] += 1
        for i in range(1,N+1):
            if out_degree[i] == 0 and in_degree[i] == N-1:
                return i
        return -1

N = 3
trust = [[1,3],[2,3],[3,1]]
obj = Solution()
ans = obj.findJudge(N,trust)
print(ans)
