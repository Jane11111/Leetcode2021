# -*- coding: utf-8 -*-
# @Time    : 2021-03-17 16:19
# @Author  : zxl
# @FileName: 131_2.py


class Solution(object):

    def ispal(self,s):
        f = True
        i = 0
        j = len(s) -1
        while i<j :
            if s[i]!=s[j]:
                f=False
            i+=1
            j-=1
        return f

    def recursivePartition(self,s,dic):
        if s in dic:
            return dic[s]
        if len(s) == 0:
            return [[]]
        if len(s) == 1:
            return [[s]]
        ans = []
        if self.ispal(s):
            ans.append([s])
        for i in range(1,len(s)):
            if self.ispal(s[:i]):
                r = self.recursivePartition(s[i:],dic)
                for item in r:
                    cur_lst = [sub_s for sub_s in item]
                    cur_lst.insert(0,s[:i])
                    ans.append(cur_lst)
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


