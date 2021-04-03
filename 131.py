# -*- coding: utf-8 -*-
# @Time    : 2021-03-17 15:45
# @Author  : zxl
# @FileName: 131.py
# import sys
# sys.setrecursionlimit(100000)


# TODO 超时

class Solution(object):

    def recursivePartition(self,s,dic):
        if len(s) == 0:
            return [[]]
        if len(s) == 1:
            return [[s]]
        if s in dic:
            return dic[s]





        ans = []
        i = 0
        j = len(s)-1
        f = True
        while i<j:
            if s[i]!=s[j]:
                f = False
            i+=1
            j-=1
        if f:
            ans.append([s])

        for i in range(len(s)-1):
            left = self.recursivePartition(s[:i+1],dic)
            right = self.recursivePartition(s[i+1:],dic)
            for l in left:
                for r in right:
                    cur = []
                    cur.extend(l)
                    cur.extend(r)
                    if cur in ans:
                        continue
                    ans.append(cur)
        dic[s] = ans
        return ans




    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        ans = self.recursivePartition(s,{})
        return ans


obj = Solution()
s = 'ssssssss'
ans = obj.partition(s)
print(ans)
