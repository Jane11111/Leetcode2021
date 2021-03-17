# -*- coding: utf-8 -*-
# @Time    : 2021-03-14 20:37
# @Author  : zxl
# @FileName: 310_2.py


class Solution(object):

    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        dic = {}
        for edge in edges:
            n1 = edge[0]
            n2 = edge[1]
            if n1 not in dic:
                dic[n1] = []
            if n2 not in dic:
                dic[n2] = []
            dic[n1].append(n2)
            dic[n2].append(n1)

        while len(dic) > 2:

            keys = list(dic.keys())
            removed_lst  = []
            for key in keys:
                if len(dic[key]) <= 1:
                    removed_lst.append(key)
            for k in keys:
                if k in removed_lst:
                    dic.pop(k)
                else:
                    for n in removed_lst:
                        if n in dic[k]:
                            dic[k].remove(n)

        ans = []
        for k in dic:
            ans.append(k)

        if len(ans) == 1:
            return ans
        if len(ans) == 2 and ans[0] > ans[1]:
            ans[0],ans[1] = ans[1],ans[0]
        if len(ans) == 0:
            ans.append(0)
        return ans

obj = Solution()
n = 6
edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
ans = obj.findMinHeightTrees(n,edges)
print(ans)